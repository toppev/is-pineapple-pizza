{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 88,
   "metadata": {},
   "outputs": [],
   "source": [
    "from keras.models import Sequential\n",
    "from keras.layers import Convolution2D\n",
    "from keras.layers import MaxPooling2D\n",
    "from keras.layers import Flatten\n",
    "from keras.layers import Dense\n",
    "from keras.optimizers import SGD\n",
    "from keras.preprocessing.image import ImageDataGenerator"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Init CNN\n",
    "classifier = Sequential()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Convolutional layer\n",
    "classifier.add(Convolution2D(32, 3, 3, input_shape=(256, 256, 3), activation='relu'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Pooling\n",
    "classifier.add(MaxPooling2D(pool_size=(2, 2)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "metadata": {},
   "outputs": [],
   "source": [
    "classifier.add(Flatten())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Full connection\n",
    "classifier.add(Dense(units=2, activation='relu'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Compile\n",
    "classifier.compile(optimizer='SGD', loss='binary_crossentropy', metrics=['accuracy'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Found 2063 images belonging to 2 classes.\n",
      "Found 20 images belonging to 2 classes.\n"
     ]
    }
   ],
   "source": [
    "batch_size = 64\n",
    "epochs = 10\n",
    "num_samples = 2000 # approximately\n",
    "\n",
    "# Fit images\n",
    "train_datagen = ImageDataGenerator(\n",
    "        rescale=1./255,\n",
    "        shear_range=0.2,\n",
    "        zoom_range=0.2,\n",
    "        horizontal_flip=True)\n",
    "\n",
    "test_datagen = ImageDataGenerator(rescale=1./255)\n",
    "\n",
    "training_set = train_datagen.flow_from_directory(\n",
    "    'dataset/training_set',\n",
    "    target_size=(256, 256),\n",
    "    batch_size=batch_size,\n",
    "    class_mode='binary')\n",
    "\n",
    "test_set = test_datagen.flow_from_directory(\n",
    "    'dataset/test_set',\n",
    "    target_size=(256, 256),\n",
    "    batch_size=batch_size,\n",
    "    class_mode='binary')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "classifier.fit_generator(\n",
    "        training_set,\n",
    "        steps_per_epoch=(num_samples // batch_size),\n",
    "        epochs=25,\n",
    "        validation_data=test_set,\n",
    "        validation_steps=2000)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Save the model\n",
    "classifier.save('model')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Test accuracy\n",
    "correct = 0\n",
    "guesses = 0\n",
    "for i in range(steps):\n",
    "    test_item = test_set.next()\n",
    "    guesses = classifier.predict(test_item[0])\n",
    "    correct = test_item[1]\n",
    "    guesses += 1\n",
    "    if round(guesses[0][0]) == correct[index]:\n",
    "        correct += 1\n",
    "        \n",
    "print('Result: ' + str(correct) + '/' + str(guesses))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
