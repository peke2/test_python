#coding: UTF-8

import numpy as np
import cv2

def load():
    img = cv2.imread('../images/IMG_1402_1024.jpg')
    cv2.imshow('画像確認', img)

    while True:
        ch = 0xFF & cv2.waitKey(0)
        if ch == 27:
            break

load()
