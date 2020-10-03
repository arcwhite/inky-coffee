#!/usr/bin/env python3

# Intended to be run every minute (or so?), this will display the next image
# the is in IMAGE_OF_DAY_DIR. This is probably too much tbh, and a better
# version of this would be more focused on outputting a single image with the
# right info on it, or doing more time-sensitive updates, but it's a fun exercise.

from PIL import Image, ImageDraw
from os import listdir, remove
from os.path import isfile, join
from inky import InkyWHAT
import random

# SYNC_DIR='/home/pi/Documents/inky-coffee/'
SYNC_DIR='/Users/arcwhite/Dropbox/Apps/inky-coffee/'
IMAGE_OF_DAY_DIR=SYNC_DIR + 'iotd/'

inky_display = InkyWHAT("red")
inky_display.set_border(inky_display.WHITE)

image_files = [f for f in listdir(IMAGE_OF_DAY_DIR) if isfile(join(IMAGE_OF_DAY_DIR, f))]

# TODO: Need some way to track which file we're currently up to?
# Let's just random-select for now!

name = random.choice(image_files)
img = Image.open(join(IMAGE_OF_DAY_DIR, name))

inky_display.set_image(img)
inky_display.show()