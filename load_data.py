import os

class LoadData:
    def __init__(self,path):
        self.path=path
        print(f'Loading data from: {path}')
    
    def getData(self,folders):
        images = []
        labels = []

        for folder in folders:
            if folder not in os.listdir(self.path):
                print(f'ERROR: {folder} is not in {self.path}')
                return

            subfolders_path = self.path+f'/{folder}'
            subfolders = os.listdir(subfolders_path)

            print(f'Searching in: {subfolders_path}')
            for subfolder in subfolders:
                for file in os.listdir(subfolders_path+f'/{subfolder}'):
                    file_path=subfolders_path+f'/{subfolder}/{file}'
                    
                    if file.endswith('.jpg'):
                        images.append(file_path)
                    if file.endswith('.txt'):
                        labels.append(file_path) #TODO: add key points read insted of path
                    
        if len(images)!=len(labels):
            print('ERROR: length of found images list is not the same as labels length')
            return
        
        print(f'Found {len(images)} items')
        return images,labels
if __name__=='__main__':

    #Data folder path
    data_folder_path = 'E:\CULANE'
    data = LoadData(data_folder_path)

    #Data folders
    data_folders = ['driver_23_30frame','driver_161_90frame','driver_182_30frame']
    images,labels = data.getData(data_folders)