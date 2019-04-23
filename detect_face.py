'''
    code for detect face
    using haarcascade
    xsufyan@gmail.com
'''

import cv2

# path to cascade
cascade_path = "model/haarcascade_frontalface_default.xml"

# create classificier
face_cascade = cv2.CascadeClassifier(cascade_path)

# open cv cam
id_cam = 0
cap = cv2.VideoCapture(id_cam)
# cap = cv2.VideoCapture("video/lny.mp4")

while cap.isOpened():
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.2, 5)
    
    print(len(faces))
    if len(faces) != 0:
        x, y, w, h = faces[0]
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,0,255), 2)

    cv2.imshow("detect ", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break
