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
                break

            subfolders_path = self.path+f'/{folder}'
            subfolders = os.listdir(subfolders_path)

            print(f'Searching in: {subfolders_path}')
            for subfolder in subfolders:
                for file in os.listdir(subfolders_path+f'/{subfolder}'):
                    file_path=subfolders_path+f'/{subfolder}/{file}'
                    
                    if file.endswith('.jpg'):
                        images.append(file_path)
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
                    
        if len(images)!=len(labels):
            print('ERROR: length of found images list is not the same as labels length')
            print(f'Found {len(images)} images and {len(labels)} labels')
            return
        
        print(f'Found {len(images)} items')
        return images,labels

if __name__=='__main__':

    #Data folder path
    data_folder_path = 'E:\CULANE'
    data = LoadData(data_folder_path)

    #Data folders
    train_folders = ['driver_23_30frame','driver_161_90frame','driver_182_30frame']
    #test_folders = ['driver_37_30frame', 'driver_100_30frame','driver_193_90frame']

    images,labels = data.getData(train_folders)
    
    #Print example data
    print(images[3], labels[3])