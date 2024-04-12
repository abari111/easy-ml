import torch
from torchvision import transforms

# Processing image
def preprocess(image):
    image = image.resize((256, 256))
    transform = transforms.ToTensor()
    image = transform(image)
    return image

#load the model
def load():
    model_path = "model.pht"
    model = torch.load(model_path)
    return model