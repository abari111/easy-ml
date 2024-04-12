import torch
from torch import nn
import torch.nn.functional as F

im_shape = (240, 240, 3)
class_nbr = 3
fil_nbr = 60
fil_size = (5, 5)
fil_size_2 = (3, 3)
pool_size = (2, 2)
nodes = 500

class RetModel(nn.Module):
    def __init__(self):
        super(RetModel, self).__init__()
        # Layer 1
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=60, kernel_size=5, padding=1)
        self.relu1 = nn.ReLU()
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=60, kernel_size=5, padding=1)
        self.relu1 = nn.ReLU()
        self.pool1 = nn.MaxPool2d(kernel_size=2, stride=2)

        # Layer 2
        self.conv2 = nn.Conv2d(in_channels=60, out_channels=30, kernel_size=3, padding=1)
        self.relu2 = nn.ReLU()
        self.pool2 = nn.MaxPool2d(kernel_size=2, stride=2)
        self.drop = nn.Dropout()
        # Fully connected layers
        # self.flatten = nn.Flatten()
        self.fc1 = nn.Linear(11970, 128)
        self.relu3 = nn.ReLU()
        self.fc2 = nn.Linear(128, 10)
        self.soft_act = nn.Softmax(dim=0)

    def forward(self, x):
        
        x = self.pool1(self.relu1(self.conv1(x)))
        x = self.pool2(self.relu2(self.conv2(x)))
        x = torch.flatten(x, 1)
        x = self.relu3(self.fc1(x))
        x = self.fc2(x)
        y = self.soft_act(x) 
        return y


class Net(nn.Module):
    
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(3, 6, 5)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = torch.flatten(x, 1) # flatten all dimensions except batch
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x



if __name__=="__main__":
    # import cv2 as cv
    # model = nn.Conv2d(3, 10, 3, stride=1)
    # img = cv.imread('sankara.jpeg')
    # img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    # print(img_rgb.shape)
    # img_tensor = torch.from_numpy(img)
    # img_tensor = img_tensor.to(torch.float)
    # img_tensor = img_tensor.permute(2,0, 1)
    # print(img_tensor.shape)
    # conv_img = model(img_tensor)
    # conv_img = conv_img.permute(2, 1, 0).detach().numpy()
    # print(conv_img.shape)
    # for i in range(10):
    #     cv.imshow('Conv'+str(i), conv_img[:, :, i])
    # cv.imshow('original', img)
    # cv.waitKey(0)
    data = torch.randn(size=(3, 256, 256))
    # print(data)
    model = Net()
    # soft_output = nn.Softmax(dim=0)
    # print(soft_output(data))  
    # print(model)