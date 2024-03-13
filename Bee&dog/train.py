import torch 
import torch.nn as nn 
import torch.optim as optim 
import torchvision.transforms as transforms
import torchvision
import pandas as pd 
from dataset import AnimalDataset, get_csv
from torch.utils.data import DataLoader

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")



# Hyperparameters
in_channel = 3
num_classes = 2
learning_rate = 3e-4
batch_size = 4
num_epochs = 10

# Dataset preparation

dataset = AnimalDataset(
    path='dataset/', 
    annotations='annot.csv', 
    transforms=transforms.ToTensor())

train_size = int(len(dataset) * 0.8)  # 80% for training
val_size = len(dataset) - train_size  # remaining 20% for validation

train_set, test_set = torch.utils.data.random_split(dataset, [train_size, val_size])
train_loader = DataLoader(dataset=train_set, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(dataset=test_set, batch_size=batch_size, shuffle=True)

# Model
model = torchvision.models.googlenet(weights=torchvision.models.GoogLeNet_Weights)

for param in model.parameters():
    param.requires_grad = False
print(model)

model.fc = nn.Linear(in_features=1024, out_features=num_classes)

# Loss and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=learning_rate, weight_decay=1e-5)

# Train network
for epoch in range(num_epochs):
    losses = []

    for batch_idx, (data, targets) in enumerate(train_loader):
        data = data.to(device=device)
        targets = targets.to(device=device)

        scores = model(data)
        loss = criterion(scores, targets)
        losses.append(loss.item())

        optimizer.zero_grad()
        loss.backward()

        optimizer.step()

    print(f"epoch {epoch}: loss={sum(losses)/len(losses)}")

save_path = "model.pht"
torch.save(model, save_path)
# print("Checking accuracy on Training Set")
# check_accuracy(train_loader, model)

# print("Checking accuracy on Test Set")
# check_accuracy(test_loader, model)
