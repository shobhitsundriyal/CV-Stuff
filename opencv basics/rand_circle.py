import numpy as np 
import cv2

canvas = np.zeros((300,300,3), dtype='uint8')

for i in range(0, 25):
    radius = np.random.randint(5,100)
    color = np.random.randint(0, 256, (3,)).tolist()
    pt = np.random.randint(0, 300, (2,))
    cv2.circle(canvas, tuple(pt), radius, color, -1)

cv2.imshow("Random Circle", canvas)
cv2.waitKey(0)
