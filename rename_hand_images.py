# coding:utf-8
# @time:2022/3/3下午6:09
# @author:sdh
import os
import glob
import shutil
hand_images_path = "/media/lessmart/work/sdh/images/"


def rename_image():
    hand_images_list = glob.glob(hand_images_path+"*.png")
    hand_images_list = sorted(hand_images_list)
    print(len(hand_images_list))

    for i in range(len(hand_images_list)):
        image_name = hand_images_list[i].split("/")[-1].split(".")[0]
        print(image_name)
        image_new_name = int(image_name)
        image_new_name = "%06d" % image_new_name
        image_new_name = str(image_new_name)+".png"

        os.rename(hand_images_list[i],hand_images_path+image_new_name)


def order_image_name():
    hand_images_list = glob.glob(hand_images_path + "*.png")
    print(len(hand_images_list))

    hand_images_list = sorted(hand_images_list)
    print(hand_images_list)

    for i in range(len(hand_images_list)):

        image_new_name = "%06d" % i
        print(image_new_name)

        image_new_name = str(image_new_name)+".png"
        os.rename(hand_images_list[i], hand_images_path + image_new_name)



if __name__ == '__main__':
    # rename_image()
    # order_image_name()
    hand_images_list = glob.glob(hand_images_path + "*.png")
    print(len(hand_images_list))

    hand_images_list = sorted(hand_images_list)
    for i in range(len(hand_images_list)):
        if i<100:
            print(hand_images_list[i])