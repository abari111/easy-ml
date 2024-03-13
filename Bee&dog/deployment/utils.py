import torch
from torchvision import transforms


def preprocess(image):

    image = image.resize((256, 256))
    transform = transforms.ToTensor()
    image = transform(image)
    return image