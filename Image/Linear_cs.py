# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 14:00:01 2019

@author: Ohida Amin Ohi
"""

import cv2
import numpy as np


img = cv2.imread('lenna.jpg',0)

print('Enter Input (r1,s1) and (r2,s2) : ')
r1 = input() #50
s1 = input() #40
r2 = input() #180
s2 = input() #190

r = [0, int(r1), int(r2), 255]
s = [0, int(s1), int(s2), 255]

cv2.imshow('input image',img)
cv2.imwrite('input_image_lin.jpg',img)

img1 = img
for i in range(img1.shape[0]):
    for j in range(img1.shape[1]):
        intense = img1[i, j]
        for k in range(len(r)-1):
            if intense<r[k+1] and intense>=r[k]:
                slope = (s[k+1]-s[k])/(r[k+1]-r[k])
                c = s[k]-slope*r[k]
                img1[i,j] = slope*intense+c 				


cv2.imshow('output image',img1)
cv2.imwrite('output_image_lin.jpg',img1)

cv2.waitKey(0)
cv2.destroyAllWindows()



