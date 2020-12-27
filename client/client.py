# import cv2
# from model import *

# cap = cv2.VideoCapture(0)

# while True:
#   ret, frame = cap.read()
#   img = show_inference_detection(frame)
#   cv2.imshow('detection', img)
#   if cv2.waitKey(1) & 0xFF == ord('q'):
#     break

import socket

try:
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  print("created socket")
except socket.error as err:
  print("Failed to create socket with error: %s".format(err))

HOST = "127.0.0.1"
PORT = 8000

# connect to server
s.connect((HOST, PORT))

print("connected to server")
