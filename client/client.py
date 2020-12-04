import cv2
from model import *

cap = cv2.VideoCapture(0)

while True:
  ret, frame = cap.read()
  img = show_inference(frame)
  cv2.imshow('detection', img)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
