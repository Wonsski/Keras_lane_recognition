import cv2
from load_data import LoadData


data_folder_path = 'E:\CULANE'
data = LoadData(data_folder_path)

#Example data folder
data_folders = ['driver_37_30frame']

images,labels = data.getData(data_folders)

for i in range(len(images)):
    img = cv2.imread(images[i])

    lines = labels[i]
    for line in lines:
        for point in line:
            cv2.circle(img, point, 10, (255,255,0))
    cv2.imshow('Preview | Press q to exit',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break