'''
    code for check function image save 
    opencv
    sufyan saori
    xsufyan@gmail.com
'''

import cv2
import os

id_cam = 0
cap = cv2.VideoCapture(id_cam)
index = 0
name = input('masukkan npm : ')
path = "foto/"+name
# check jika folder sudah ada
if os.path.isdir(path) :
    y = os.listdir(path)
    if (y) :
        index = sorted([int(os.path.splitext(x)[0]) for x in y])[-1]+1
        print(index)
else:
    os.mkdir("foto/"+name)

while cap.isOpened():
    ret, frame = cap.read()
    if frame is None:
        break
    cv2.imshow('Camera', frame)
    key = cv2.waitKey(1) & 0xFF
    
    # save image
    if key == ord("c"):
        print('take picture')
        namefile = os.path.join (path+"/"+str(index)+'.png')
        cv2.imwrite(namefile, frame)
        index += 1
    if key == ord("q"):
        cv2.destroyAllWindows()
        break
