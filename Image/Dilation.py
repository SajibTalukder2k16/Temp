# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 11:35:43 2021

@author: NLP Lab
"""


import numpy as np
from cv2 import cv2

original = cv2.imread('th.jpg')
#cv2.imshow('ori',original)
#cv2.waitKey(0)
gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
(thresh,bina) = cv2.threshold(gray,120,255,cv2.THRESH_BINARY)
cv2.imshow('input',bina)
#cv2.waitKey(0)
def conv_transform(image):
    image_copy = image.copy()
    
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            image_copy[i][j] = image[image.shape[0]-i-1][image.shape[1]-i-1]
    return image_copy 

filt = np.array([[1,1,1],[1,1,1], [1,1,1]])

filt=conv_transform(filt)
S = bina.shape
F = filt.shape
bina2 = bina/255
R = S[0]+F[0]-1
C = S[1]+F[1]-1
N = np.zeros((R,C))

for i in range(S[0]):
    for j in range(S[1]):
        N[i+2,j+2]=bina2[i,j]
        
for i in range(S[0]):
    for j in range(S[1]):
       k = N[i:i+F[0],j:j+F[1]]
       result = (k==filt)
       final = np.any(result==True)
       if final:
           bina2[i,j]=1
       else:
           bina2[i,j]=0
           
cv2.imshow('Dilated Image',bina2)

output = bina2 - bina
cv2.imshow('Dialated Edge', output)

cv2.waitKey(0)
cv2.destroyAllWindows()


















           
           
        
