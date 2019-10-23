import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io

from copy import deepcopy

pic = io.imread('9-6-1999-main(chs.-4,3,2).png')

red_channel = deepcopy(pic)
green_channel = deepcopy(pic)
blue_channel = deepcopy(pic)

red_channel[:,:,1]=0
red_channel[:,:,2]=0

green_channel[:,:,0]=0
green_channel[:,:,2]=0

blue_channel[:,:,0]=0
blue_channel[:,:,1]=0

fig, ax = plt.subplots(ncols=2, nrows=2)

ax[0,0].imshow(pic)
ax[0,0].set_title('Original')

ax[0,1].imshow(red_channel)
ax[0,1].set_title('Red Channel')

ax[1,0].imshow(green_channel)
ax[1,0].set_title('Green Channel')

ax[1,1].imshow(blue_channel)
ax[1,1].set_title('Blue Channel')



plt.show()


import skimage.filters as sk_filters
image = io.imread('6_8-19-2018_LakePowell_Main.png', as_gray=True)

result = sk_filters.roberts(image)
plt.imshow(result, cmap='Greys')
plt.title('Roberts Edge Detection')
plt.show()


result = sk_filters.sobel(image)
plt.imshow(result, cmap='hot')
plt.title('sobel Edge Detection')
plt.show()


result = sk_filters.scharr(image)
plt.imshow(result, cmap='Wistia')
plt.title('scharr Edge Detection')
plt.show()



result = sk_filters.prewitt(image)
plt.imshow(result, cmap='cool')
plt.title('Prewitt Method')
plt.show()


#canny edge detection
import cv2
img = cv2.imread('10-22-2013_main(chs. 5,4,3).png',0)
edges = cv2.Canny(img,100,200)

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()
