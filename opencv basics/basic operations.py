import argparse
import cv2



ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='Enter image path')# for program 
args = vars(ap.parse_args())



image = cv2.imread('image.jpg')

print('Height = {}pixels'.format(image.shape[0]))
print('Width = {}pixels'.format(image.shape[1]))
print('Channels = {}'.format(image.shape[2]))



cv2.imshow('Image Title',image)
cv2.waitKey(5000)
cv2.imwrite('new.jpg', image)






