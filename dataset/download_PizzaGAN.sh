#!/bin/sh

# Downloads pizzaGANdata dataset and runs categorize.py
# Takes quite a long time
# There are only ~80 pineapple pizzas so might

cd dataset

wget http://pizzagan.csail.mit.edu/pizzaGANdata.zip

unzip pizzaGANdata.zip

python3 categorize.py