from flask import Flask, request, flash, redirect, render_template

from keras.models import load_model

model = load_model('model')
model.summary()
