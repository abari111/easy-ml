import os

import matplotlib.pyplot as plt
import cv2 as cv
import pandas as pd
from PIL import Image
import torch
from torch.utils.data import(
    Dataset,
    DataLoader,
)


os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

LABELS = {0: 'bee', 1: 'dog'}

def get_csv(path, animals=None):
    annotations = {'path': [], 'label': []}
    labels = {}
    targets_dirs = animals if animals else os.listdir(path)
    index = 0

    for dir in targets_dirs:
        files_names  = os.listdir(os.path.join(path, dir))
        labels[index] = dir
        for image in files_names:
            annotations['path'].append(os.path.join(dir, image))
            annotations['label'].append(index)
        index+=1
    annotations = pd.DataFrame(annotations)

    return annotations.to_csv('annot.csv'), labels

class AnimalDataset(Dataset):

    def __init__(self, path, annotations, transforms=None):
        self.path = path 
        self.annotations = pd.read_csv(annotations)
        self.transforms = transforms

    def __len__(self,):
        return len(self.annotations) 

    def __getitem__(self, index):
        image_path = os.path.join(self.path, self.annotations.iloc[index, 1])
        image = Image.open(image_path)
        image = image.resize((256, 256))
        if self.transforms:
            image = self.transforms(image)
        targets = torch.tensor(int(self.annotations.iloc[index, 2]))
        return image, targets

if __name__ == "__main__":
    annotations, labels= get_csv("dataset/", ['bee', 'dog'])
    annotations = pd.read_csv('annot.csv')
    dataset = AnimalDataset('dataset', 'annot.csv') 
    
    ax = plt.imshow(dataset[100][0])
    plt.title(labels[dataset[100][1].item()])
    plt.show()
