# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 01:08:13 2021

@author: zobay
"""

import cv2
import numpy as np
import math

img = cv2.imread("lena.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("input", img)

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        img.itemset((i,j), 255 - img.item(i,j))
        
cv2.imshow("neg transformation", img)

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        img.itemset((i,j), 31.875*math.log(img.item(i,j), 2))


cv2.imshow("Log transformation", img)


for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        img.itemset((i,j), math.pow(2, img.item(i,j)/31.875)-1)

cv2.imshow("iverse Log transformation", img)
cv2.waitKey(0)
cv2.destroyAllWindows()