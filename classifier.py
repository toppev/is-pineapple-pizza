#!/usr/bin/env python
# coding: utf-8

# In[88]:


from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.preprocessing.image import ImageDataGenerator

# In[90]:


# Init CNN
classifier = Sequential()

# In[92]:


# Convolutional layer
classifier.add(Convolution2D(32, 3, 3, input_shape=(256, 256, 3), activation='relu'))

# In[94]:


# Pooling
classifier.add(MaxPooling2D(pool_size=(2, 2)))

# In[96]:


classifier.add(Flatten())

# In[98]:


# Full connection
classifier.add(Dense(units=2, activation='relu'))

# In[100]:


# Compile
classifier.compile(optimizer='SGD', loss='binary_crossentropy', metrics=['accuracy'])

# In[102]:


batch_size = 64
epochs = 10
num_samples = 2000  # approximately

# Fit images
train_datagen = ImageDataGenerator(
    rescale=1. / 255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1. / 255)

training_set = train_datagen.flow_from_directory(
    'dataset/training_set',
    target_size=(256, 256),
    batch_size=batch_size,
    class_mode='binary')

test_set = test_datagen.flow_from_directory(
    'dataset/test_set',
    target_size=(256, 256),
    batch_size=batch_size,
    class_mode='binary')

# In[106]:


classifier.fit_generator(
    training_set,
    steps_per_epoch=(num_samples // batch_size),
    epochs=25,
    validation_data=test_set,
    validation_steps=2000)

# In[ ]:


# Save the model
classifier.save('model')

# In[ ]:


# Test accuracy
correct = 0
guesses = 0
for i in range(steps):
    test_item = test_set.next()
    guesses = classifier.predict(test_item[0])
    correct = test_item[1]
    guesses += 1
    if round(guesses[0][0]) == correct[index]:
        correct += 1

print('Result: ' + str(correct) + '/' + str(guesses))
