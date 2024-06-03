
import os
from pathlib import Path
from typing import Set, Dict

from utils import check_files_ext
from magika import Magika 

CFG = {
    'png': 'Photos',
    'jpeg': 'Photos',
    'jpg': 'Photos',
    'c': 'C lang',
    'python': 'Python',
}

def _init(CFG: dict) ->None:
    for key in CFG.keys():
        try: 
            os.mkdir(key)
        except Exception as e:
            print(e)

def manage_dir(dir_path: str, cfg: dict = CFG) -> None:
    _init(cfg)
    outputs = check_files_ext(dir_path)

    for path, ext in zip(outputs['paths'], outputs['labels']):
        dir_name = cfg[ext]