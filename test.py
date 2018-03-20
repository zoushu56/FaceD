#!/usr/bin/env python
# coding:utf-8

from PIL import Image, ImageDraw, ImageFont

# 打开图片
im = Image.open('/Users/mac/Desktop/1.png')
draw = ImageDraw.Draw(im)
fontsize = min(im.size) / 8
font = ImageFont.truetype('/Users/mac/Desktop/田相岳圆楷体.ttf', fontsize)
draw.text((im.size[0] - fontsize*2, 0), '100', font=font, fill=(0, 100, 100))
im.save('/Users/mac/Desktop/2.png', 'png')