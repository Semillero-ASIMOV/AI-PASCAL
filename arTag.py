import imutils
import argparse
import numpy as np
import cv2
import cv2.aruco as aruco
from cv2 import 
cap = cv2.VideoCapture(0)
def centroid(*points):
    x_coords = [p[0] for p in points]
    y_coords = [p[1] for p in points]
    _len = len(points)
    centroid_x = int(sum(x_coords)/_len)
    centroid_y = int(sum(y_coords)/_len)
    return [centroid_x, centroid_y]

def printCentroid(corners):
    centroidPoint = centroid(corners[0][0][0], corners[0][0][1], corners[0][0][2], corners[0][0][3])
    print(centroidPoint)
    cv2.circle(frame, (centroidPoint[0], centroidPoint[1]), 5, (255, 255, 0), -1)
    cv2.putText(frame, "Centroid", (centroidPoint[0] - 20, centroidPoint[1] - 20),
        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (204, 255, 0), 2)

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_1000)
    arucoParameters = aruco.DetectorParameters_create()
    corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=arucoParameters)
    frame = aruco.drawDetectedMarkers(frame, corners, ids)
    if len(corners) > 0: 
        printCentroid(corners)
    cv2.imshow('Display', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
