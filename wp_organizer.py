#!/usr/bin/env python

#######################################################################
## wp_organizer.py - A wallpaper organizer
#######################################################################
## License: MIT
#######################################################################
## Author: Pedro H. G. Souto
## Version: 0.2
## Mmaintainer: Pedro H. G. Souto
## Email: phgsouto (a) gmail dot com
## Status: development
#######################################################################

import os

try:
    from PIL import Image
except ImportError:
    raise ImportError('Pillow not found.')


WP_TEMP_DIR = 'C:\\Users\\Pedro\\wp\\temp'
WP_FINAL_DIR = 'C:\\Users\\Pedro\\wp'


def main():
    print('~~ wp_organizer -- A wallpaper organizer! ~~')
    temp_wallpapers = os.listdir(WP_TEMP_DIR)

    image_and_ratios = {}

    for f in temp_wallpapers:
        if not is_image(f):
            temp_wallpapers.remove(f)
        else:
            image_and_ratios[f] = get_ratio(
                get_img_dimensions(WP_TEMP_DIR + '\\' + f))

    for image, ratio in image_and_ratios.items():
        move_files(image, ratio)


def is_image(filename=None):
    if type(filename).__name__ == 'str':
        if filename.split('.')[-1] in ['png', 'jpg', 'jpeg']:
            return True
    return False


def get_img_dimensions(path=None):
    size = (0, 0)
    if path and os.path.isfile(path):
        img = Image.open(path)
        size = img.size
        img.close()
    return size


def get_ratio(size):
    common_ratios = {
        1.20: '6_5',
        1.25: '5_4',
        1.33: '4_3',
        1.36: '11_8',
        1.37: '11_8',
        1.50: '3_2',
        1.51: '3_2',
        1.58: '16_10',
        1.59: '16_10',
        1.60: '16_10',
        1.66: '5_3',
        1.78: '16_9',
        2.35: '21_9',
        2.36: '21_9',
        2.37: '21_9',
        2.38: '21_9',
        2.39: '21_9',
        2.40: '21_9',
        0.56: '9_16',
        0.62: '10_16',
        0.42: '9_21'
    }
    if type(size).__name__ == 'tuple':
        ratio = float("{0:.2f}".format(size[0] / size[1]))
        if ratio in common_ratios:
            return common_ratios[ratio]
        else:
            return 'unusual'
    return -1


def move_files(filename, directory):
    dir_path = WP_FINAL_DIR + '\\' + directory
    file_old_path = WP_TEMP_DIR + '\\' + filename
    file_new_path = dir_path + '\\' + filename

    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    os.rename(file_old_path, file_new_path)


if __name__ == '__main__':
    main()

# EOF
