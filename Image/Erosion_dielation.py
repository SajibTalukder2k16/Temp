# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 09:33:56 2021

@author: snazm
"""
import numpy as np
import cv2
import copy

img = cv2.imread("th.jpg")

cv2.imshow("input", img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", gray)
(thresh,binary) = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

binary_copy=copy.deepcopy(binary)
binary_copy = binary_copy/255

filt_kernel = np.ones((3,3))

binary_erosion = copy.deepcopy(binary)

in_shape = binary_erosion.shape
filter_shape = filt_kernel.shape


binary_erosion = binary_erosion/255

binary_dialation = copy.deepcopy(binary_erosion)


Rows = in_shape[0]+filter_shape[0]-1
Columns = in_shape[1]+filter_shape[1]-1


N = np.zeros(shape=(Rows,Columns))



for i in range(in_shape[0]):
    for j in range(in_shape[1]):
        p = int((2*filter_shape[0]-1)/2)
        q = int((filter_shape[1]-1)/2)
        N[i+p,j+q] = binary_erosion[i,j]
        

"""for i in range(in_shape[0]):
    for j in range(in_shape[1]):
        k = N[i:i+filter_shape[0],j:j+filter_shape[1]]
        result = (k == filt_kernel)
        final = np.all(result == True)
        if final:
            binary_erosion[i,j] = 1
        else:
            binary_erosion[i,j] = 0

cv2.imshow("erosion", binary_erosion)"""

for i in range(in_shape[0]):
    for j in range(in_shape[1]):
        k = N[i:i+filter_shape[0],j:j+filter_shape[1]]
        result = (k == filt_kernel)
        final = np.any(result == True)
        if final:
            binary_dialation[i,j] = 1
        else:
            binary_dialation[i,j] = 0
            

cv2.imshow("dialation", binary_dialation)
binary_copy= binary_dialation-binary_copy
cv2.imshow("Boundary detection", binary_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()