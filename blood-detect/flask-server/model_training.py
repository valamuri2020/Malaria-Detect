"""
This is a .py version of the Colab notebook at 
https://colab.research.google.com/drive/1ZZgkpYXL33pKm4fZ-7tjoWiXDO9o_jUY?usp=sharing

"""
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import math 

my_data_dir = '/content/cell_images'
os.listdir(my_data_dir)

test_path = my_data_dir+'/test'
train_path = my_data_dir+'/train'

os.listdir(test_path)

os.listdir(train_path)

from matplotlib.image import imread

os.listdir(train_path+'/parasitized/')[0]

infected_cell = train_path+'/parasitized'+'/C45P6ThinF_IMG_20151130_160135_cell_216.png'

infected_cell = imread(infected_cell)

plt.imshow(infected_cell)

healthy_cell = train_path + '/uninfected/' + os.listdir(train_path+'/uninfected')[0]
healthy_cell = imread(healthy_cell)
plt.imshow(healthy_cell)

dim1 = []
dim2 = []

for image_filename in os.listdir(test_path+'/uninfected'):
    img = imread(test_path+'/uninfected'+'/'+image_filename)
    d1,d2,colors = img.shape
    dim1.append(d1)
    dim2.append(d2)

sns.jointplot(dim1,dim2, color='purple' )

image_shape = (math.floor(np.mean(dim1)), math.floor(np.mean(dim2)), 3)

from tensorflow.keras.preprocessing.image import ImageDataGenerator

# artificially expanding data set by randomly applying transformations on them
# randomly choose a % between 0-10 and scale the transformation by that factor
image_generator = ImageDataGenerator(rotation_range=20, 
                                     width_shift_range=0.1, 
                                     height_shift_range=0.1,
                                     zoom_range=0.1,
                                     shear_range=0.1,
                                     horizontal_flip=True,
                                     fill_mode='nearest') 


# pixel values are normalized
plt.imshow(infected_cell)

# example of a randomly transformed image
plt.imshow(image_generator.random_transform(infected_cell))

image_generator.flow_from_directory(train_path)

image_generator.flow_from_directory(test_path)


from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, MaxPool2D, Dropout, Flatten

########## Model ##########
# larger image sizes require more convolutional layers to detect patterns

model = Sequential()

model.add(Conv2D(filters=32, kernel_size=(3,3), input_shape=image_shape, activation='relu'))
model.add(MaxPool2D(pool_size=(2,2)))

model.add(Conv2D(filters=64, kernel_size=(3,3), input_shape=image_shape, activation='relu'))
model.add(MaxPool2D(pool_size=(2,2)))

model.add(Conv2D(filters=64, kernel_size=(3,3), input_shape=image_shape, activation='relu'))
model.add(MaxPool2D(pool_size=(2,2)))

model.add(Flatten())

model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5)) # helps reduce overfitting

model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

########## Model ##########


from tensorflow.keras.callbacks import EarlyStopping

early_stop = EarlyStopping(monitor='val_loss', patience=2)

# smaller batch size is proportional to a longer training time
batch_size = 16 

train_image_gen = image_generator.flow_from_directory(train_path, 
                                                      target_size=image_shape[:2], 
                                                      color_mode='rgb',
                                                      batch_size=batch_size,
                                                      class_mode='binary')

test_image_gen = image_generator.flow_from_directory(test_path, 
                                                      target_size=image_shape[:2], 
                                                      color_mode='rgb',
                                                      batch_size=batch_size,
                                                      class_mode='binary',
                                                     shuffle=False) # do NOT shuffle labels for test set

train_image_gen.class_indices

results = model.fit_generator(train_image_gen, 
                              epochs=10, 
                              validation_data=test_image_gen, 
                              callbacks=[early_stop])

pred = model.predict_generator(test_image_gen)

# if probability > 70%, classify as uninfected
predictions = pred >= 0.7 

from sklearn.metrics import classification_report, confusion_matrix

print(classification_report(test_image_gen.classes, predictions))

print(confusion_matrix(test_image_gen.classes, predictions))