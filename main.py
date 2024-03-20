#!/usr/bin/python3
import cv2
import numpy as np
image = cv2.imread('png.png')
ret,image = cv2.threshold(image,138,255,cv2.THRESH_BINARY)
cv2.imshow('1',image)
cv2.waitKey(0)
