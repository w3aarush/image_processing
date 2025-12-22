import numpy as np
import cv2 as c

def sme(image1, image2):
    error = np.sum((image1.astype('float')-image2.astype('float'))**2)
    error /= float(image1.shape[0]*image2.shape[1])
    return error

img1 = c.imread('stop1.jpg')
img2 = c.imread('stop1.jpg')

error = sme(img1, img2)

if round(error)==0:
    print("Image is similar.")
else:
    print("Image is not similar.")
