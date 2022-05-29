import os
import numpy as np
import cv2
import time
from tqdm import tqdm

class LoadData:
    def __init__(self,path):
        self.path=path
        print(f'Dataset folder: {path}')
    
    def getData(self,folders):
        images = []
        labels = []
        
        print(f'\nStarted collecting data from folders: {folders}')
        print('Status:')

        for folder in folders:
            start = time.time()
            if folder not in os.listdir(self.path):
                print(f'ERROR: {folder} is not in {self.path}')
                break

            subfolders_path = self.path+f'/{folder}'
            subfolders = os.listdir(subfolders_path)

            print(f'Collecting from: {subfolders_path}')
            for subfolder in tqdm(subfolders):
                for file in os.listdir(subfolders_path+f'/{subfolder}'):
                    file_path=subfolders_path+f'/{subfolder}/{file}'
                    
                    if file.endswith('.jpg'):
                        #image loading and resizing
                        image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)

                        image = cv2.resize(image, (256,256))
                        images.append(image)

                        #extracting labels from files
                        label_path = file_path[:-4]+'.lines.txt'

                        lines = []
                        with open(label_path) as f:
                            for line in f.readlines():
                                line = line.split()
                                
                                points = []
                                for i in range(0, len(line)//2, 2):
                                    x = line[i]
                                    y = line[i+1]
                                    points.append((int(float(x)),int(float(y))))
                                
                                lines.append(points)

                        labels.append(lines)
            end = time.time()

            time_elapsed = end-start
            print(f'Time elapsed: {int(time_elapsed//60)} min {int(time_elapsed%60)} sec')

        #cohesion handler
        if len(images)!=len(labels):
            print('ERROR: length of found images list is not the same as labels list length')
            print(f'Found {len(images)} images and {len(labels)} labels')
            return
        
        print(f'Found {len(images)} items')
        return images,labels
    
    def loadAndSaveData(self,folders,filename,location='data/'):
        if os.path.exists(f'{location}{filename}.npz'):
            return self.loadDataFromFile(filename)
        
        images,labels = self.getData(folders)

        data = np.asanyarray([images,labels],dtype=object)

        if not os.path.exists(location):
            os.mkdir(location)
        
        print(f'Saving data into {location}{filename}.npz...')
        np.savez_compressed(f'{location}{filename}.npz',data)

        print(f'Saved data from: {folders} into {location}{filename}.npz')
        
        return images,labels

    def loadDataFromFile(self,filename,location='data/'):
        if not os.path.exists(f'{location}{filename}.npz'):
            print(f'ERROR: Not found file {location}{filename}.npz')
            return

        print(f'Loading data from file: {location}{filename}.npz...')
        images,labels = np.load(f'{location}{filename}.npz', allow_pickle=True)['arr_0']

        print(f'Successfully loaded data from: {location}{filename}.npz')

        return images,labels

if __name__=='__main__':

    #Dataset folder path
    dataset_folder_path = 'D:\CULANE'
    data = LoadData(dataset_folder_path)

    #Data folders
    train_folders = ['driver_23_30frame','driver_161_90frame','driver_182_30frame']
    test_folders = ['driver_37_30frame', 'driver_100_30frame','driver_193_90frame']

    #Load and save data in data/
    x_train, y_train = data.loadAndSaveData(train_folders,'train_data')
    x_test, y_test = data.loadAndSaveData(test_folders,'test_data')