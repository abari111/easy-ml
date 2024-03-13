import torch
import torchvision
from torchvision import transforms
from torch.utils.data import Dataset, DataLoader
from utils import RetDataset, CleanRetDataset, display_dataset

device = "cuda" if torch.cuda.is_available() else "cpu"
# Loading dataset
ret_transforms = torchvision.transforms.Compose(
        [
            torchvision.transforms.ToTensor()
        ]
    )
dataset = RetDataset(
                data_path='datasets/ret_dataset', 
                annot_file_path="datasets/ret_annot.csv",)
processed_dataset = CleanRetDataset(dataset=dataset, transforms=ret_transforms)

display_dataset(dataset)
# Models
model = torchvision.models.resnet50(weights="IMAGENET1K_V1")
model.fc = torch.nn.Linear(in_features=2048, out_features=5)

for params in list(model.parameters())[:-1]:
    params.trainable = False
# Hyperparameters
lr = 1e-3
batch_size = 34
num_epoch = 10 
dataloader = DataLoader(processed_dataset, batch_size=batch_size, shuffle=True)
optimizer = torch.optim.Adam(model.parameters(), lr=lr)
criterion = torch.nn.CrossEntropyLoss()

# Training

for epoch in range(num_epoch):
    losses = []
    for x_train, y_train in dataloader:
        y_pred = model(x_train)

        optimizer.zero_grad()
        loss = criterion(y_pred, y_train.flatten())
        losses.append(loss.item())

        loss.backward()
        optimizer.step()
    
    print(f"epoch={epoch:.2f} --------------- loss={sum(losses)/len(losses)}")
# Testing

# if __name__=="__main__":
#     model.eval()
#     data = torch.randn(size=(1, 3, 28, 28))
#     print(model(data))