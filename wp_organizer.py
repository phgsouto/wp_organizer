#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------- #
#                                    Imports                                   #
# ---------------------------------------------------------------------------- #
import os
import argparse
from pathlib import Path
try:
    from PIL import Image
except ImportError:
    raise ImportError('Pillow not found.')

# ---------------------------------------------------------------------------- #
#                                 Package Info                                 #
# ---------------------------------------------------------------------------- #
__package__ = "wp_organizer"
__author__ = "Pedro H. G. Souto"
__license__ = "MIT"
__version__ = "0.2.1"
__maintainer__ = "Pedro H. G. Souto"
__email__ = "phgsouto (a) gmail dot com"
__status__ = "development"

# ---------------------------------------------------------------------------- #
#                             Function declarations                            #
# ---------------------------------------------------------------------------- #
def main():

    parser = argparse.ArgumentParser(description='A simple wallpaper organizer')
    parser.add_argument("-V", "--version", 
                        help="print version information",
                        action="store_true")
    parser.add_argument("-d", "--dest",
                        help="destination directory")
    args = parser.parse_args()

    if args.version:
        print(__package__,"version",__version__)
    
    if args.dest:
        destination_directory = Path(args.dest)
    else:
        destination_directory = Path(os.getcwd())

    temp_wallpapers = os.listdir(Path(os.getcwd()))
    image_and_ratios = {}

    for f in temp_wallpapers:
        if not is_image(f):
            temp_wallpapers.remove(f)
        else:
            image_and_ratios[f] = get_ratio(
                get_img_dimensions(destination_directory / f))

    if len(image_and_ratios) > 0:
        for image, ratio in image_and_ratios.items():
            move_files(destination_directory, ratio, image)
    else:
        print('There is no images in the current directory')


def is_image(filename=None):
    image_formats = ['ase', 'art', 'bmp', 'blp', 'cd5', 'cit', 'cpt', 'cr2', 
                     'cut', 'dds', 'dib', 'djvu', 'egt', 'exif', 'gif', 'gpl', 
                     'grf', 'icns', 'ico', 'iff', 'jng', 'jpeg', 'jpg', 'jfif', 
                     'jp2', 'jps', 'lbm', 'max', 'miff', 'mng', 'msp', 'nitf', 
                     'ota', 'pbm', 'pc1', 'pc2', 'pc3', 'pcf', 'pcx', 'pdn', 
                     'pgm', 'PI1', 'PI2', 'PI3', 'pict', 'pct', 'pnm', 'pns', 
                     'ppm', 'psb', 'psd', 'pdd', 'psp', 'px', 'pxm', 'pxr', 
                     'qfx', 'raw', 'rle', 'sct', 'sgi', 'rgb', 'int', 'bw', 
                     'tga', 'tiff', 'tif', 'vtf', 'xbm', 'xcf', 'xpm', '3dv', 
                     'amf', 'ai', 'awg', 'cgm', 'cdr', 'cmx', 'dxf', 'e2d', 
                     'egt', 'eps', 'fs', 'gbr', 'odg', 'svg', 'stl', 'vrml', 
                     'x3d', 'sxd', 'v2d', 'vnd', 'wmf', 'emf', 'art', 'xar', 
                     'png', 'webp', 'jxr', 'hdp', 'wdp', 'cur', 'ecw', 'iff', 
                     'lbm', 'liff', 'nrrd', 'pam', 'pcx', 'pgf', 'sgi', 'rgb', 
                     'rgba', 'bw', 'int', 'inta', 'sid', 'ras', 'sun', 'tga' ]
    
    if type(filename).__name__ == 'str':
        if filename.split('.')[-1] in image_formats:
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


def move_files(directory, subdirectory, filename):
    dir_path = directory / subdirectory
    file_old_path = Path(os.getcwd()) / filename
    file_new_path = dir_path / filename

    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    os.rename(file_old_path, file_new_path)


if __name__ == '__main__':
    main()

# EOF
