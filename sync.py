#!/usr/bin/env python3
import datetime
import hashlib
import fnmatch
from PIL import Image, ImageDraw
from os import listdir, remove
from os.path import isfile, join

SYNC_DIR='/home/pi/Documents/inky-coffee/'
INPUT_FILE_DIR=SYNC_DIR + 'images/'
IMAGE_OF_DAY_DIR=SYNC_DIR + 'iotd/'

# today = datetime.date.today()
# tomorrow = today + datetime.timedelta(days=1)

# today_dir = today.isoformat()
# tomorrow_dir = today.isoformat()

# Get a list of the input images
input_files = [f for f in listdir(INPUT_FILE_DIR) if isfile(join(INPUT_FILE_DIR, f))]

# Parse into a dict of [imagename, hash]
# input_images = [[f, hashlib.sha3_224(f.encode('utf8')).hexdigest()] for f in input_image_files]

expected_files = {}
hasher = hashlib.md5()
for filename in input_files:
    with open(INPUT_FILE_DIR+filename, 'rb') as open_file:
        buf = open_file.read()
        hasher.update(buf)
        expected_files[filename] = hasher.hexdigest()

print(expected_files)

for name, hash_value in expected_files.items():
    filename, extension = name.split('.')
    expected_name = filename + '_' + hash_value + '.' + extension
    # If imagename_hash.ext exists in IMAGE_OF_DAY_DIR, skip to next image
    if isfile(join(IMAGE_OF_DAY_DIR, expected_name)):
        continue
    # If imagename_NOT-THIS-HASH.ext exists in IMAGE_OF_DAY_DIR, delete it
    for delete_me in fnmatch.filter(listdir(IMAGE_OF_DAY_DIR), filename + '_*.' + extension):
        # print(IMAGE_OF_DAY_DIR+delete_me)
        remove(join(IMAGE_OF_DAY_DIR, delete_me))
    img = Image.open(join(IMAGE_OF_DAY_DIR, name))
    w, h = img.size
    h_new = 300
    w_new = int((float(w) / h) * h_new)
    w_cropped = 400
    



# Generate the new image
