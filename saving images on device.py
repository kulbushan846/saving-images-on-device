"""
saving images using skimage

"""

from skimage import io
img = io.imread('om.jpg')   #reading image 

from skimage import filters  #importing filters 
gaussian_img = filters.gaussian(img,sigma = 3)  # using gaussian filters

"""
saving images
"""

io.imsave("E:\PYTHON\image programs\gaussian_img.jpg", gaussian_img)

from skimage import img_as_ubyte
gaussian_img_byte = img_as_ubyte(gaussian_img) #gaussian image converted into byte
io.imsave("E:\PYTHON\image programs\gaussian_img_byte.jpg", gaussian_img_byte)

""""saving images using opencv-image"""
import cv2
cv2.imwrite("E:\PYTHON\image programs\gaussian_img_cv2.jpg", img)