# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 11:18:36 2020

@author: NLP Lab
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy as dpc

img_inp=cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)
a_min = np.min(img_inp)
a_max = np.max(img_inp)

for i in range (img_inp.shape[0]):
    for j in range(img_inp.shape[1]):
        img_inp[i][j] = (((img_inp[i][j]-a_min)/(a_max-a_min))*255)
img_inp = img_inp.astype(np.uint8)
img = dpc(img_inp)


each_intensity = [0 for i in range (256)]
each_intensity_out = [0 for i in range (256)]
histogram = [0.0 for i in range (256)]
histogram_out = [0.0 for i in range (256)]
Hist = [0.0 for i in range(256)]
Hist_out = [0.0 for i in range(256)]
s = [0.0 for i in range (256)]    


image_size=img.shape[0]*img.shape[1]

##histogram calculation for input
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        x = img.item(i,j)
        each_intensity[x] += 1
        
for i in range(256):
    histogram[i] = each_intensity[i] / image_size

## CDF calculation for input
sum_hist = 0

for i in range(256):
    sum_hist = sum_hist + histogram[i]
    Hist[i] = sum_hist + histogram[i]
    s[i]=round(sum_hist*255)


## output update
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        x=img[i][j]
        img[i][j]=s[x]

##CDF of output
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        x = img.item(i,j)
        each_intensity_out[x] += 1
        
for i in range(256):
    histogram_out[i] = each_intensity_out[i]

sum_hist = 0

for i in range(256):
    sum_hist = sum_hist + histogram_out[i]
    Hist_out[i] = sum_hist
    
cv2.imshow("input image",img_inp)
plt.hist(img_inp.ravel(),256,[0,256])
plt.title("Input image")
plt.show()

plt.plot(Hist)
plt.title("Input historam")
plt.show()

cv2.imshow("Output image",img)
plt.hist(img.ravel(),256,[0,256])
plt.title("Output image original")
plt.show()

plt.plot(Hist_out)
plt.title("Output histogram")
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
