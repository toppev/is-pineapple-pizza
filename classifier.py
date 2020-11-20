#!/usr/bin/env python
# coding: utf-8

# In[1]:


import keras
from keras.models import Sequential
from keras.layers import experimental
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.optimizers import SGD


# In[2]:


# Init CNN
model = Sequential([
        experimental.preprocessing.RandomFlip("horizontal"),
        experimental.preprocessing.RandomRotation(0.1),
    ]
)


# In[3]:


image_size = (256, 256)


# In[4]:


# First convolution layer + pooling
model.add(Conv2D(32, 3, 3, input_shape=(256, 256, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))


# In[5]:


# One more time + 2 pools (works better idk why)
model.add(Conv2D(64, 3, 3, input_shape=(256, 256, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(MaxPooling2D(pool_size=(2, 2)))


# In[6]:


# Flatten step
model.add(Flatten())


# In[8]:


# Densely connected layers
model.add(Dense(128, activation='relu'))
model.add(Dense(1, activation='sigmoid'))


# In[9]:


# Compile with given optimizer
opt = SGD(lr=0.001) # might change this
model.compile(optimizer=opt, loss='binary_crossentropy', metrics=['accuracy'])


# In[10]:


batch_size = 32
# Subset 20% for training
training_set = keras.preprocessing.image_dataset_from_directory(
    "dataset/training_set",
    validation_split=0.2,
    subset="training",
    seed=42069,
    image_size=image_size,
    batch_size=batch_size,
)
test_set = keras.preprocessing.image_dataset_from_directory(
    "dataset/training_set",
    validation_split=0.2,
    subset="validation",
    seed=42069,
    image_size=image_size,
    batch_size=batch_size,
)


# In[11]:


model.fit(training_set,
        epochs=30, # less is probably enough
        validation_data=test_set,
        batch_size=batch_size)


# In[ ]:


# Save the model
model.save('model')


# In[ ]:


# Test accuracy
results = model.evaluate(test_set, batch_size=64)
print("test loss/accuracy:", results)


# In[ ]:


# Visualize a few results
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import os
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

model = load_model('model')

for i in range(10):
    filename = 'dataset/examples/' + str(i) + '.jpg'
    test_img = image.load_img(filename, target_size=image_size)
    test_img = image.img_to_array(test_img)
    test_img = np.expand_dims(test_img, axis=0)
    
    result = model.predict(test_img)
    acc = result[0][0]
    is_pineapple = acc > 0.5
    label = 'Pineapple Pizza' if is_pineapple else 'Not Pineapple Pizza'
   
    img = mpimg.imread(filename)
    imgplot = plt.imshow(img)
    plt.text(x=0, y=-2, s= label + '(' + str(result[0][0]) + ')', fontsize=15)
    plt.show()


# In[ ]:





# In[ ]:




