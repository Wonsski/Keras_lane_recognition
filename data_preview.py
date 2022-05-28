import cv2
from load_data import LoadData


data_folder_path = 'D:\CULANE'
data = LoadData(data_folder_path)

images,labels = data.loadDataFromFile('test_data')

for i in range(len(images)):

    lines = labels[i]
    for line in lines:
        for point in line:
            cv2.circle(images[i], point, 10, (255,255,0))
    cv2.imshow('Preview | Press q to exit',images[i])
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break