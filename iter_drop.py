# coding:utf-8
# @time:2022/3/4上午11:10
# @author:sdh
import os
import glob
import shutil
import copy


def ori_images_from_dorplist(ori_images_path, droplist_txt_file):
    """

    :param ori_images_path:
    :param droplist_txt_file:
    :return:
    """
    ori_images_list = glob.glob(ori_images_path + "*.png")

    ori_images_list = sorted(ori_images_list)
    ori_images_list_copy = copy.copy(ori_images_list)

    drop_index_list = []
    len_ori_images_list = len(ori_images_list)

    print(len_ori_images_list)  # 99552
    with open(droplist_txt_file, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for p,line in enumerate(lines):
            if p == 0:
                str_index_list = line.split(",")
                str_index_list = str_index_list[0:len(str_index_list)-1]
                print(len(str_index_list))  # 1079

                for i in str_index_list:
                    drop_index_list.append(int(i))
    #
    print(drop_index_list)
    for i in range(len_ori_images_list - 1, -1, -1):
        if i > len(drop_index_list) - 1:
            continue
        else:
            ori_images_list.remove(ori_images_list[drop_index_list[i]])

    print(len(ori_images_list))

    for image_path in ori_images_list_copy:
        if image_path not in ori_images_list:
            src = image_path
            dst = "move_images_file/" + src.split("/")[-1]
            print(src,dst)
            shutil.move(image_path, dst)


if __name__ == '__main__':
    ori_images_from_dorplist("/media/lessmart/work/sdh/images/", "index.txt")
