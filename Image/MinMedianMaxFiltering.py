import cv2
import numpy as np
img = cv2.imread('lena.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow("image",img)
imgout= cv2.imread('lena.jpg',cv2.IMREAD_GRAYSCALE)
for i in range(1,img.shape[0]-1):
    for j in range(1,img.shape[1]-1):
        min=255
        for x in range(-1,1):
            for y in range(-1,1):
                  a = img.item(i+x, j+y)
                  if a<min:
                      min=a
        m=min
        imgout.itemset((i,j),m)
cv2.imshow("MINFilter",imgout)

img = cv2.imread('lena.jpg',cv2.IMREAD_GRAYSCALE)
imgout= cv2.imread('lena.jpg',cv2.IMREAD_GRAYSCALE)
for i in range(2,img.shape[0]-2):
    for j in range(2,img.shape[1]-2):
        nn = []
        for x in range(-2,+2):
            for y in range(-2,+2):
                  a = img.item(i+x, j+y)
                  nn.append(a)
        nn.sort()
        m=nn[12]
        nn.clear()
        imgout.itemset((i,j),m)
cv2.imshow("MEDIANFilter",imgout)

img = cv2.imread('lena.jpg',cv2.IMREAD_GRAYSCALE)
imgout= cv2.imread('lena.jpg',cv2.IMREAD_GRAYSCALE)
for i in range(2,img.shape[0]-2):
    for j in range(2,img.shape[1]-2):
        max=0
        for x in range(-2,+2):
            for y in range(-2,+2):
                  a = img.item(i+x, j+y)
                  if a>max:
                     max=a
        m=max
        imgout.itemset((i,j),m)

cv2.imshow("MAXFilter",imgout)

img = cv2.imread('lena.jpg',cv2.IMREAD_GRAYSCALE)
imgout= cv2.imread('lena.jpg',cv2.IMREAD_GRAYSCALE)
for i in range(2,img.shape[0]-2):
    for j in range(2,img.shape[1]-2):
        sum=0
        for x in range(-2,+2):
            for y in range(-2,+2):
                  a = img.item(i+x, j+y)
                  sum=sum+a
                 
        m=sum/25
        imgout.itemset((i,j),m)

cv2.imshow("Average",imgout)

cv2.waitKey(0)
cv2.destroyAllWindows()