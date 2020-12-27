# imports
from __future__ import print_function
from PIL import Image, ImageTk
import tkinter as tk
import threading
import imutils
from imutils.video import VideoStream
import datetime
import cv2
import os

class PhotoBoothApp:
  def __init__(self, vs):
    self.vs = vs
    self.frame = None
    self.thread = None
    self.stopEvent = None

    self.root = tk.Tk()
    self.panel = None

    self.stopEvent = threading.Event()
    self.thread = threading.Thread(target=self.videoLoop, args={})
    self.thread.start()

    self.root.wm_title("PyImageSearch PhotoBooth")
    self.root.wm_protocol("WM_DELETE_WINDOW", self.onClose)

  def videoLoop(self):
    try:
      while not self.stopEvent.isSet():
        self.frame = self.vs.read()
        self.frame = imutils.resize(self.frame, width=300)

        image = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        image = cv2.resize(image, (800, 600))
        image = Image.fromarray(image)
        image = ImageTk.PhotoImage(image)

        if self.panel is None:
          self.panel = tk.Label(image=image)
          self.panel.image = image
          self.panel.pack(side="left", padx=10, pady=10)
        else:
          self.panel.configure(image=image)
          self.panel.image = image
    except RuntimeError as e:
      print("[INFO] caught a RuntimeError:", e)
  
  def onClose(self):
    print("[INFO] closing...")
    self.vs.stop()
    self.stopEvent.set()
    self.root.quit()

print("[INFO] warming up the camera")
vs = VideoStream().start()

pba = PhotoBoothApp(vs)
pba.root.mainloop()
