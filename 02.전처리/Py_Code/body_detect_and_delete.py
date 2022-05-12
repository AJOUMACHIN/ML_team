import os
import sys
import cv2


dir_path = ['./크롤링/긴팔티셔츠', './크롤링/민소매티셔츠', './크롤링/반팔티셔츠', './크롤링/피케_카라티셔츠', './크롤링/후드티셔츠']

lower_body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "./haarcascade_lowerbody.xml")

for in_dir in dir_path:
    cnt = 0
    for file in os.listdir(in_dir):
        if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg") or file.endswith(".bmp") or file.endswith(".tiff") or file.endswith(".tif"):
            img = cv2.imread(in_dir + '/' + file)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            lower_bodys_cascade = lower_body_cascade.detectMultiScale(gray, 1.01, 10, 0, minSize=(100, 100))

            if len(lower_bodys_cascade) > 0:
                os.remove(in_dir + '/' + file)
                print("deleted in " + in_dir + '/' + file)
                print("detected body count: " + str(len(lower_bodys_cascade)))
                cnt += 1
    print("deleted " + str(cnt) + " files in " + in_dir)