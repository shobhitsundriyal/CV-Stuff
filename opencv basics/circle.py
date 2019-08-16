import numpy as np 
import cv2

canvas = np.zeros((300,300,3), dtype='uint8')

blue = (255,0,0)
cv2.circle(canvas, (100,100), 30, blue, -1)
cv2.imshow('Canvas',canvas)
cv2.waitKey(0)

canvas = np.zeros((300,300,3), dtype='uint8')
(X,Y) = (canvas.shape[1]//2, canvas.shape[0]//2)
white = (255,255,255)
for i in range(0,175,25):
    cv2.circle(canvas, (X,Y), i, white)
cv2.imshow('Concentric Cicle', canvas)
cv2.waitKey(0)