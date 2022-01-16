import numpy as np
import cv2
import matplotlib.pyplot as plt

def my_filter(img, kernel):
    l = img.shape[0]
    w = img.shape[1]
    k = kernel.shape[0]
    img = cv2.copyMakeBorder(img,k//2,k//2,k//2,k//2,cv2.BORDER_CONSTANT,value=255)
    
    dst = np.zeros((l,w))

    for i in range(l):
        for j in range(w):
            sum_ = 0.0
            for p in range(k):
                for q in range(k):
                    x = i+p
                    y = j+q
                    sum_ = sum_ + img[x][y]*kernel[p][q]
            dst[i][j] = sum_
            
    cv2.imshow('without scaling laplacian image',dst)
    cv2.imwrite('non_scaled_lap.jpg',dst)
    dst = cv2.normalize(dst,dst, 0,255,cv2.NORM_MINMAX)
    return np.uint8(dst)      
            


kernel = np.array([[0,-1,0],[-1,4,-1],[0,-1,0]])
plt.imshow(kernel, interpolation='none')

img = cv2.imread('lena.jpg',0)
cv2.imshow('input image',img)
cv2.imwrite('lap_input.jpg',img)


dst = my_filter(img, kernel)
cv2.imshow('laplacian image',dst)
cv2.imwrite('scaled_lap.jpg',dst)


cv2.waitKey(0)
cv2.destroyAllWindows()