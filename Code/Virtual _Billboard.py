# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 15:35:58 2021

@author: Sonu
"""

import cv2
import numpy as np

#Defining variables to store coordinates where the second image has to be placed
positions=[] 

#Mouse callback function to store the coordinates of the image points clicked
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONUP:
        positions.append([x,y])
        print(x, ' ', y)
        # displaying the coordinates on the image window 
        font = cv2.FONT_HERSHEY_SIMPLEX 
        cv2.putText(building, str(x) + ',' +str(y), (x,y), font, 1, (255, 0, 0), 2) 
        cv2.imshow('image', building)

  
# Reading the two images and storing it in variables img and dp
building = cv2.imread('building.jpg')

cv2.imshow('image', building) 
cv2.setMouseCallback('image', draw_circle) 
cv2.waitKey(0)
cv2.destroyAllWindows() 

dp = cv2.imread('dp.jpg')
cv2.waitKey(20000)
cv2.destroyAllWindows()

height, width = building.shape[:2]
h1,w1 = dp.shape[:2]

#Points should be clicked in the same order as per the order of other set of points else homography will not be correct.
pts1=np.float32([[0,0],[0,h1],[w1,h1],[w1,0]])
pts2=np.float32(positions)

#Finding the homography
h, mask = cv2.findHomography(pts1, pts2, cv2.RANSAC,5.0)
height, width, channels = building.shape

#Warping one of the image so that both of the image will be aligned on the same plane and have same perspective view.
im1Reg = cv2.warpPerspective(dp, h, (width, height))

#Creating a black mask with size equal to the src image size
mask2 = np.zeros(building.shape, dtype=np.uint8)

roi_corners2 = np.int32(positions)

#Creating a white mask
channel_count2 = building.shape[2]  
ignore_mask_color2 = (255,)*channel_count2

#Filling the black mask with a white mask whose size is as per the coordinates of the warped target image
cv2.fillConvexPoly(mask2, roi_corners2, ignore_mask_color2)
cv2.imshow("Filled Mask", mask2)
cv2.waitKey(10000)
cv2.destroyAllWindows()

#Finding the inverse of the filled black mask created
mask2 = cv2.bitwise_not(mask2)
cv2.imshow("Inverted Mask", mask2)
cv2.waitKey(10000)
cv2.destroyAllWindows()

#Applying the inverted filled black mask on src image
masked_image2 = cv2.bitwise_and(building, mask2)
cv2.imshow("Blackened Image", masked_image2)
cv2.waitKey(10000)
cv2.destroyAllWindows()

#Using Bitwise or to merge the two images or blend the two images.
final = cv2.bitwise_or(im1Reg, masked_image2)
cv2.imshow("Warped Image", final)
cv2.waitKey(10000)
cv2.destroyAllWindows()
cv2.imwrite('final.png',final)