"""
Method 1

import cv2
import numpy as np

image1 = cv2.imread("test1.png",0)
image2 = cv2.imread("test2.pmg",0)

difference = cv2.subtract(image1,image2)
result = not np.any(difference)

if result is True:
	print("The images are same")
else:
	cv2.imwrite("result.png",difference)
	print("The images are different")

	"""

# Method 2
from PIL import Image, ImageChops
img1 = Image.open('s1987.png')
img2 = Image.open('s2018.png')

diff = ImageChops.difference(img1,img2)

if diff.getbbox():
	diff.show()