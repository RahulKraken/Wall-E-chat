import cv2
# default cascadeclassifier in opencv
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# capture video from source 0 - default device - webcam
video = cv2.VideoCapture(0)

# a : number_of_frames
a = 1

while True:
    a = a+1
    check, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=None, minNeighbors=10)

    # for loop get coordinates of face position
    for x, y, w, h in faces:
        # constantly draws a rectangle around face coordinates
        frame = cv2.rectangle(frame, (x,y), (x+w,y+h),(0,250,0),3)
        # x,y,x+w,y+h coordinates which can be used to align camera to keep person in frame
    #for_loop_ends-------------------------------------------------------------------------------------------

    cv2.imshow("capturing", frame)
    key = cv2.waitKey(1)

    #--------------------------------- PRESS Q TO QUIT VIDEO_WINDOW -----------------------------------------
    if key == ord('q'):
        break
# while_loop_ends--------------------------------------------------------------------------------------------

print(a)
video.release()
cv2.destroyAllWindows()