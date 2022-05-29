import cv2
from load_data import LoadData


data_folder_path = 'D:\CULANE'
data = LoadData(data_folder_path)

images,labels = data.loadDataFromFile('test_data')

for i in range(len(images)):

    lines = labels[i]
    img = cv2.resize(images[i], (1640,590))
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

    for line in lines:
        for point in line:
            cv2.circle(img, point, 10, (0,255,0))
            
    cv2.imshow('Preview | Press q to exit',img)

    if cv2.waitKey(5) & 0xFF == ord('q'):
            break