# coding:utf-8
# @time:2022/3/3下午3:48
# @author:sdh
import requests  ##导入requests
import random
import time


import glob
images_list_hand = glob.glob("/media/lessmart/work/sdh/images/"+"*.png")
images_list_hand = sorted(images_list_hand)

images_list_print = glob.glob("png_images/"+"*.png")
images_list_print = sorted(images_list_print)

print(len(images_list_hand),len(images_list_print))

images_list_hand_i = []
for i in range(len(images_list_hand)):
    images_list_hand_i.append(images_list_hand[i].split("/")[-1])

images_list_print_i = []
for i in range(len(images_list_print)):
    images_list_print_i.append(images_list_print[i].split("/")[-1])


for x in images_list_print_i:
    if x not in images_list_hand_i:
        print(x)

