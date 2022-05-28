import os
import sys
import cv2


dir_path = ['../배경삭제/긴팔티셔츠', '../배경삭제/민소매티셔츠', '../배경삭제/반팔티셔츠', '../배경삭제/피케_카라티셔츠', '../배경삭제/후드티셔츠']

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + './haarcascade_frontalface_default.xml')

for in_dir in dir_path:
    cnt = 0
    facecnt = 0
    for file in os.listdir(in_dir):
        if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg") or file.endswith(".bmp") or file.endswith(".tiff") or file.endswith(".tif"):
            img = cv2.imread(in_dir + '/' + file)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            faces_cascade = face_cascade.detectMultiScale(gray, 1.3, 5)

            if len(faces_cascade) >= 1:
                for (x, y, w, h) in faces_cascade:
                    delete_faces = img[y+h:, 0:]
                    cv2.imwrite(in_dir + "/" + file, delete_faces)
                print("얼굴 잘림!")
                facecnt += 1
                print(in_dir, file, facecnt)
            else:
                cnt += 1
                print(in_dir, file, cnt)