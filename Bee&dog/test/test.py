import os

import torch 
from torchvision import transforms
from PIL import Image


dogs_images = os.listdir('dataset/dog')
labels = {0: 'bee', 1: 'dog'}


for file_img in dogs_images:
    img_path = "bee.jpeg"
    image = Image.open(img_path)
    
    image = image.resize((256, 256))
    transform = transforms.ToTensor()
    image = transform(image)
    
    model = torch.load('../models/model.pht')
    model.eval()
    
    with torch.no_grad():
        scores = model(image.unsqueeze(0))
        scores = torch.nn.functional.softmax(scores, dim=1)
        _ , pred = scores.max(1)
        print(labels[pred.item()], f': {_}')
        
    model.train()