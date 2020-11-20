# Script to put pinepple pizzas and other pizzas in separate directories
import os
from shutil import copyfile

images = sorted(os.listdir("pizzaGANdata/images"))

max_images = 5000
test_images = 50

pineapples = 0
not_pineapples = 0

with open("pizzaGANdata/imageLabels.txt") as f:
    index = 0
    for line in f:
        index += 1

        main_dir = 'training_set'
        is_pineapple = line.endswith('1\n')
        if (is_pineapple and pineapples < test_images) or (not is_pineapple and not_pineapples < test_images):
            main_dir = 'test_set'
        target = main_dir + '/not_pineapple/' + str(not_pineapples) + '.jpg'

        if is_pineapple:
            target = main_dir + '/pineapple/' + str(pineapples) + '.jpg'
            if pineapples >= max_images:
                continue
            pineapples += 1
        else:
            if not_pineapples >= max_images:
                continue
            not_pineapples += 1
        if len(images) > index:
            copyfile('pizzaGANdata/images/' + images[index - 1], target)

print('Pineapples: ' + str(pineapples))
print('Not pineapples: ' + str(not_pineapples))
