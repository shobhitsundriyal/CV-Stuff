import cv2
import numpy as np 
import os
import time

#yolo_files -> coco.names -> person, yolov3.cfg, yolov3.weights

labels_path = os.path.sep.join(['yolo_files', 'coco.names'])
LABELS = open(labels_path).read().strip().split('\n')

weight_path = os.path.sep.join(['yolo_files', 'yolov3.weights'])
config_path = os.path.sep.join(['yolo_files', 'yolov3.cfg'])

print('Loading the model...') 

net = cv2.dnn.readNetFromDarknet(config_path, weight_path)

i = 1
a = 63
cap = cv2.VideoCapture(0)
while True:
    if i != 1:
        ret, image = cap.read()
    if i == 1:
        time.sleep(5)
        ret, image = cap.read()
        backdrop = image
        i = 420
        continue

    #image = cv2.imread('image.jpg')
    #image = cv2.resize(image, (640,480))

    (H, W) = image.shape[:2]

    ln = net.getLayerNames()
    ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]

    blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (416, 416),
    swapRB=False, crop=False)

    net.setInput(blob)
    layerOutputs = net.forward(ln)

    boxes = []
    confidences = []
    classIDs = []


    for output in layerOutputs:
        for detection in output:

            scores = detection[5:]
            classID = np.argmax(scores)
            confidence = scores[classID]


            if confidence > 0.5:


                box = detection[0:4] * np.array([W, H, W, H])
                (centerX, centerY, width, height) = box.astype("int")


                x = int(centerX - (width / 2))
                y = int(centerY - (height / 2))

                boxes.append([x, y, int(width), int(height)])
                confidences.append(float(confidence))


    idxs = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.3)
    diff = None

    if len(boxes) > 0:

        for i in idxs.flatten():

            (x, y) = (boxes[i][0], boxes[i][1])
            (w, h) = (boxes[i][2], boxes[i][3])
            #diff = cv2.absdiff(backdrop, image)
            cv2.rectangle(image, (x, y), (x + w, y + h), (a,a,a), cv2.FILLED)
            
    
    img = cv2.add(backdrop, image)//2
    #diff = cv2.absdiff(img, image)
    #mask = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Mask", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()