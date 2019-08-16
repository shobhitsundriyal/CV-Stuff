import numpy as np 
import cv2

canvas = np.zeros((300,300,3), dtype='uint8')

green = (0,255,0)
cv2.line(canvas, (0,0), (300,300), green)
cv2.imshow('Canvas',canvas)
cv2.waitKey(0)

red = (0,0,255)
cv2.rectangle(canvas, (10,10), (30,30), green)
cv2.imshow('Canvas',canvas)
cv2.waitKey(0)

cv2.rectangle(canvas, (30,30), (100,130), red, -1)
cv2.imshow('Canvas',canvas)
cv2.waitKey(0)
