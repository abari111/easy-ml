""" All intermediate functions are packed here"""

import os

import pandas as pd
from pandas import DataFrame
import torch
from torch.utils.data import Dataset
from torchvision.transforms import transforms, ToTensor, Compose
from PIL import Image

def balance_data(df:DataFrame, n_classes=5, n_samples:int=200, save:bool=True, dir_path:str=None) -> DataFrame:
    """Balance the dataset with n_samples of each classes samples """
    data_per_labels = {}
    for label in range(n_classes):
        data = df[df['diagnosis'] == label]
        data_per_labels[label] = data[:n_samples]

    data_stats = {i: len(data) for i, data in data_per_labels.items() }
    balanced_data = pd.concat(data_per_labels.values(), ignore_index=True)
    
    if save:
        file_name = f'annot_{n_samples}.csv'
        if dir_path is None:
            dir_path = ''
        file_path = os.path.join(dir_path, file_name)
        
        balanced_data.to_csv(file_path, index=False)
    
    return balanced_data

class RetDataset(Dataset):
    """load retinopathy dataset"""
    def __init__(self,d_path:str, annot_path:str=None, transforms=None) -> None:
        self.annots = pd.read_csv(annot_path)
        self.d_path = d_path
        self.transforms = transforms
    
    def __len__(self, ) -> int:
        return len(self.annots)
    
    def __getitem__(self, idx)->torch.Tensor:
        filename, label = self.annots.iloc[idx]
        file_path = os.path.join(self.d_path, filename + '.png')
        img = Image.open(file_path)
        
        if self.transforms:
            img_tensor = self.transforms(img)
        else:
            img_tensor = ToTensor()(img) 
        
        return img_tensor, torch.tensor(label)

class GenRetSample:
    """ Generate randomly dataset sample: img, target"""
    def __init__(self, dataset):
        self.dataset = dataset
        self.index = 0
    
    def __iter__(self, ):
        return self
    
    def __next__(self):
        if len(self.dataset) > self.index:
            self.index += 1
            return self.dataset[self.index]
        else :
            raise StopIteration()
    
def display_data(dataset):
    pass