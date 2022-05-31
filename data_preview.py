import cv2
from load_data import LoadData


data_folder_path = 'D:\CULANE'
data = LoadData(data_folder_path)

images,labels = data.loadDataFromFile('train_data')

for i in range(len(images)):

    lines = labels[i]
    img = cv2.resize(images[i], (1640,590))
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

    cv2.line(img, (labels[i][0],labels[i][1]), (labels[i][4],labels[i][5]), (0,255,0), 4)

    for x in range(0,len(labels[i]),2):
        point = (labels[i][x],labels[i][x+1])
        cv2.circle(img, point, 10, (0,0,255),-1)
            
    cv2.imshow('Preview | Press q to exit',img)

    if cv2.waitKey(5) & 0xFF == ord('q'):
            break