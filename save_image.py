'''
    code for check function image save 
    opencv
    sufyan saori
    xsufyan@gmail.com
'''

import cv2

id_cam = 0
cap = cv2.VideoCapture(id_cam)
index = 0
name = input('masukkan nama orang : ')

while cap.isOpened():
    ret, frame = cap.read()
    if frame is None:
        break
    cv2.imshow('Camera', frame)
    key = cv2.waitKey(1) & 0xFF
    
    # save image
    if key == ord("c"):
        namefile = name+str(index)+'.png'
        cv2.imwrite(namefile, frame)
    if key == ord("q"):
        cv2.destroyAllWindows()
        break
