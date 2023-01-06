# -*- coding: utf-8 -*-
# @Time    : 3/27/2019 21:54
# @Author  : MARX·CBR
# @File    : 微信Dat文件转图片.py

import os

s_out_path = r"D:\WeChat_Decode\\"

def image_decode(f, fn, dest_floder):
    dat_read = open(f, "rb")
    # out='P:\\'+fn+".png"
    out = dest_floder + fn + ".jpg"
    print(out)
    png_write = open(out, "wb")
    for now in dat_read:
        for nowByte in now:
            newByte = nowByte ^ 0x75
            png_write.write(bytes([newByte]))
    dat_read.close()
    png_write.close()


def findFile(f, dest_floder):
    fsinfo = os.listdir(f)
    for fn in fsinfo:
        temp_path = os.path.join(f, fn)
        if not os.path.isdir(temp_path):
            print('文件路径: {}'.format(temp_path))
            print(fn)
            image_decode(temp_path, fn, dest_floder)
        else:
            ...


running_path = r"F:\XXX\WeChat Files\XXX\Data\\"
findFile(running_path, s_out_path)
