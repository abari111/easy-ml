from torch.utils.data import Dataset
import torch
import torchvision
import pandas as pd
from PIL import Image
import os
from preprocess import RetNormalize
import matplotlib.pyplot as plt
import random
import json

labels_mapping = {0 : 'No DR', 1 : 'Mild', 2 : 'Moderate', 3 : 'Severe', 4 : 'Proliferative DR' }
os.environ['KMP_DUPLICATE_LIB_OK']='True'

class RetDataset(Dataset):
    def __init__(self, data_path, annot_file_path) -> any:
        self.__root = data_path
        self.__annot = pd.read_csv(annot_file_path)
    
    def __sizeof__(self) -> int:
        return len(self._annot)
    
    def __len__(self) -> int:
        return len(self.__annot)

    def __getitem__(self, index) -> tuple:
        file_name = self.__annot.iloc[index, 0] + '.png'
        try :
            img_path = os.path.join(self.__root, file_name)
            sample = Image.open(img_path)
            label = self.__annot.iloc[index, 1]
        except Exception as e:
            pass
        return sample, label


class CleanRetDataset(RetDataset):
    def __init__(self,*,  data_path=None, annot_file_path=None,  transforms=None, dataset=None):
        self.flag = None
        if data_path and annot_file_path:
            super().__init__(data_path, annot_file_path)
            self.flag = True
        elif dataset:
            self.__dataset = dataset 
            self.flag = False
        else:
            raise TypeError("None type")
        self.__transforms = transforms
    
    def __len__(self) -> int:
        if self.flag:
            return super().__sizeof__()
        else:
            return len(self.__dataset)

    def __sizeof__(self) -> int:
        if self.flag:
            return super().__sizeof__()
        else:
            return len(self.__dataset)

    def __get_dataset_1(self, index) -> tuple:
        sample, label = super().__getitem__(index)
        sample = sample.resize(size=(256, 256))
        sample = self.__transforms(sample)
        label = torch.tensor([label])
        return sample, label
    
    def __get_dataset_2(self, index) ->tuple:
        sample, label = self.__dataset[index]
        sample = sample.resize(size=(256, 256))
        sample = self.__transforms(sample)
        label = torch.tensor([label])
        return sample, label

    def __getitem__(self, index) -> tuple:
        if self.flag:
            return self.__get_dataset_1(index)
        else:
            return self.__get_dataset_2(index)

def train(model, dataloader, criterion, optimizer, num_epoch=10, device="cpu"):
    model.to(device)
    for epoch in range(num_epoch):
        losses = []

        for x_train, y_train in dataloader:
            x_train.to(device)
            y_train.to(device)

            y_pred = model(x_train)

            optimizer.zero_grad()
            loss = criterion(y_pred, y_train.flatten())
            losses.append(loss.item())

            loss.backward()
            optimizer.step()
        print(f"epoch={epoch} --------------- loss={sum(losses)/len(losses)}")

def display_dataset(dataset, k=6):
    fig, axes = plt.subplots(2, 3)
    images_idx = random.choices(range(len(dataset)), k=k)
    i = 0
    j = 0
    for image_idx in images_idx:
        image, label_idx = dataset[image_idx]
        axes[i][j].imshow(image)
        axes[i][j].set_title(labels_mapping[label_idx])
        axes[i][j].axis('off')
        j+=1
        if j  == k/2:
            j = 0
            i += 1

        
    
    plt.tight_layout()
    plt.show()

def serialize_data(data, file_name="ret_data.json"):
    data_dict = {'ret_data': list(data)}
    serialized_data = json.dumps(data_dict)

    with open(file_name, 'rw') as json_file:
        json_file.write(serialized_data)


if __name__=="__main__":
    ret_transforms = torchvision.transforms.Compose(
        [
            torchvision.transforms.ToTensor()
        ]
    )
    dataset = RetDataset(data_path="datasets/ret_dataset", annot_file_path="datasets/ret_annot.csv")
    cleaned_dataset = CleanRetDataset(transforms=ret_transforms,dataset=dataset)
    serialize_data(dataset)
    print(len(dataset))
    # dataset = CleanRetDataset(data_path="datasets/ret_dataset", annot_file_path="datasets/ret_annot.csv", transforms=Ret_transforms)
    display_dataset(dataset)