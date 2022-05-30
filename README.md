# Keras_lane_recognition

Based on: https://xingangpan.github.io/projects/CULane.html

The goal of this project is to create a model that can predict road lane lines. Work is in progress.

Author: Radosław Rajda

<br>

# Loading the data

Make sure you are using 64-bit version of Python to avoid memory error.

Data structure of CULane dataset
```
CULane [dataset folder]
    - driver_23_30frame
    - driver_161_90frame [training data folders]
    - driver_182_30frame

    - driver_37_30frame
    - driver_100_30frame [testing data folders]
    - driver_193_90frame
```

## Data load initiation
```
from load_data import LoadData

data = LoadData(dataset_folder_path) # CULane folder
```

## getData()

The function takes an array of data folders and returns two arrays: one of loaded (256,256) grayscale images and second loaded with each detected lane points

Usage:
```
x_data, y_data = data.getData([data folders])

# Example
test_folders = ['driver_37_30frame', 'driver_100_30frame','driver_193_90frame']
x_test, y_test = data.getData(test_folders)
```

## loadAndSaveData()

This function works similar to the getData() function, but additionally saves the loaded arrays to compressed .npz files. The default location of saved .npz files is 'data/'. The location can be changed by using 'location=' flag.

Usage:
```
x_data, y_data = data.loadAndSaveData([data folders],[filename])

# Example
train_folders = ['driver_23_30frame','driver_161_90frame','driver_182_30frame']
x_train, y_train = data.loadAndSaveData(train_folders,'train_data')
```

## loadDataFromFile()

This function, as the name says, loads the data from previously saved .npz files. The default location of saved .npz files is 'data/'. The location can be changed by using 'location=' flag.

Usage:
```
x_data, y_data = data.loadDataFromFile([file_name])

# Example
x_test,y_test = data.loadDataFromFile('test_data')
```

# Data preview
You can preview your loaded data using data_preview.py opencv script.