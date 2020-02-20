import cv2
import numpy as np 

cap = cv2.VideoCapture(0)
height = 480
width = 640
dim = (width, height)

backdrop = cv2.imread('backdrop.jpg') 
backdrop = cv2.resize(backdrop, dim)

while True:
    _, frame = cap.read()

    
    img_hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV) # change to hsv for mask extraction

    #mask
    mask_hsv = cv2.inRange(img_hsv, np.array([0, 0, 0]), np.array([180, 255, 120]))

    masked = np.copy(frame)
    masked[mask_hsv==0] = [0, 0, 0]

    background = np.copy(backdrop)
    background[mask_hsv != 0] = [0, 0, 0]

    combined = masked + background
    
    cv2.imshow('video', combined)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()