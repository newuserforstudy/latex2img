# coding:utf-8
# @time:2022/3/4下午4:45
# @author:sdh
from PIL import Image

import os
import glob


def get_white_background_images(convert=True):
    """
    get white background
    :param convert:
    :return:
    """
    if convert:
        ori_images_path = "/media/lessmart/work/sdh/math/print_math/"
        ori_images_path_list = glob.glob(ori_images_path + "*.png")
        ori_images_path_list = sorted(ori_images_path_list)

        for i, img_path in enumerate(ori_images_path_list):

            img_name = img_path.split("/")[-1]
            img = Image.open(img_path)
            img = img.convert('RGBA')
            sp = img.size
            width = sp[0]
            height = sp[1]
            print(sp)
            for yh in range(height):
                for xw in range(width):
                    dot = (xw, yh)
                    color_d = img.getpixel(dot)
                    if color_d[3] == 0:
                        color_d = (255, 255, 255, 255)
                        img.putpixel(dot, color_d)

            img.save(os.path.join(white_background_images_path, img_name))


if __name__ == '__main__':
    white_background_images_path = "white_background_images/"
    get_white_background_images()
