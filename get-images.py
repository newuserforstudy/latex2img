# coding:utf-8
# @time:2022/3/3下午4:38
# @author:sdh
# coding:utf-8
# @time:2022/3/3下午3:48
# @author:sdh
import requests
import random
import time
import shutil
import cairosvg
import matplotlib.pyplot as plt

png_images_path = "png_images/"
svg_images_path = "svg_images/"
drop_index = []
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/'
                  '537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36'}  # 浏览器请求头(大部分网站没有这个请求头会报错、请务必加上哦)

all_url = 'https://math.now.sh/?from='  # 开始的URL地址

latex_path = "/media/lessmart/work/backups/latex_data/im2latex/formulas.lst"
with open(latex_path, "r", encoding="utf-8") as f:
    lines = f.readlines()
    for i, line in enumerate(lines):

        all_url = 'https://math.now.sh/?from=%s ' % line
        try:
            start_html = requests.get(all_url, headers=headers)  # 使用requests中的get方法来获取all_url(就是这个地址)的内容 headers为上面设置的请求头、请务必参考requests官方文档解释

            n = '%06d' % i
            print("正在处理第：%d张图像" % i)
            n = str(n)
            f = open(svg_images_path+'%s.svg' % n, 'wb')  # 写入多媒体文件必须要 b 这个参数！！必须要！！
            f.write(start_html.content)  # 多媒体文件要是用conctent哦！
            f.close()

            cairosvg.svg2png(url=svg_images_path+'%s.svg' % n, write_to=png_images_path+'%s.png' % n)

        except Exception as e:
            print("跳过%d" % i)
            with open("index.txt", "a") as f:
                f.write(f'{i},')




