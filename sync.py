#!/usr/bin/env python3
import datetime
import hashlib
import fnmatch
from PIL import Image, ImageDraw
from os import listdir, remove
from os.path import isfile, join

# SYNC_DIR='/home/pi/Documents/inky-coffee/'
SYNC_DIR='/Users/arcwhite/Dropbox/Apps/inky-coffee/'
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
BLOCKSIZE = 65536
for filename in input_files:
    with open(INPUT_FILE_DIR+filename, 'rb') as open_file:
        buf = open_file.read(BLOCKSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = open_file.read(BLOCKSIZE)
        expected_files[filename] = hasher.hexdigest()

print(expected_files)

for name, hash_value in expected_files.items():
    filename, extension = name.split('.')
    expected_name = filename + '_' + hash_value
    # If imagename_hash.ext exists in IMAGE_OF_DAY_DIR, skip to next image
    if isfile(join(IMAGE_OF_DAY_DIR, expected_name, '.', extension)):
        continue
    # If imagename_NOT-THIS-HASH.ext exists in IMAGE_OF_DAY_DIR, delete it
    for delete_me in fnmatch.filter(listdir(IMAGE_OF_DAY_DIR), filename + '_*.' + extension):
        # print(IMAGE_OF_DAY_DIR+delete_me)
        remove(join(IMAGE_OF_DAY_DIR, delete_me))
    img = Image.open(join(INPUT_FILE_DIR, name))
    w, h = img.size
    h_new = 300
    w_new = int((float(w) / h) * h_new)
    w_cropped = 400
    img = img.resize((w_new, h_new), resample=Image.LANCZOS)
    x0 = (w_new - w_cropped) / 2
    x1 = x0 + w_cropped
    y0 = 0
    y1 = h_new
    img = img.crop((x0, y0, x1, y1))
    pal_img = Image.new("P", (1, 1))
    pal_img.putpalette((255, 255, 255, 0, 0, 0, 255, 0, 0) + (0, 0, 0) * 252)
    img = img.convert('RGB').quantize(palette=pal_img)
    img.save(IMAGE_OF_DAY_DIR + expected_name + '.png', 'PNG')
