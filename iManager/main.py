from magika import Magika
from pathlib import Path
import os


if __name__=='__main__':
    dir_path = "test/folder_1"
    list_files = os.listdir(dir_path)
    files_path = [Path(dir_path + '/' + file_name) for file_name in list_files]
    model =Magika()
    results = model.identify_paths(files_path)
    outputs = {'paths':[], 'labels':[], 'scores':[]}

    for res in results:
        outputs['paths'] = res.path
        outputs['labels'] = res.output.ct_label 
        outputs['scores'] = res.output.score
    
    print(outputs)