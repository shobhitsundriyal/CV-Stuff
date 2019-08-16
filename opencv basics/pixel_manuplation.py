import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='Enter image path')# for program 
args = vars(ap.parse_args())

image = cv2.imread('image.jpg')

(b,g,r) = image[0,0]
print('pixel at 0,0 has values {}r ,{}b ,{}g '.format(r,g,b))

image[0,0] = (0,0,255)
(b,g,r) = image[0,0]
print('pixel at 0,0 has values {}r ,{}b ,{}g '.format(r,g,b))

corner = image[0:100, 0:100]
cv2.imshow('Corner', corner)
cv2.waitKey(0)

image[0:100, 0:100] = (0,255,0)
cv2.imshow('Updated', image)
cv2.waitKey(0)