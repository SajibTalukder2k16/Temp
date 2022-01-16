# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 08:00:25 2019

@author: Asus
"""
import cv2
import numpy as np
img = cv2.imread('lena.png',cv2.IMREAD_GRAYSCALE)

x=float(input("Please input the value of gamma: "))

cv2.imshow("image",img)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        a=img.item(i,j)
        b=((np.power(a,x))*255)/(np.power(255,x))
        img.itemset((i,j),b)
cv2.imshow("Gamma",img)
cv2.waitKey(0)
cv2.destroyAllWindows()