# 라이브러리 호출
import os
import numpy as np
from PIL import Image

# 이미지 리 사이징 하기
targetdir = r"../크롤링/피케_카라티셔츠"  # 해당 폴더 설정
files = os.listdir(targetdir)
if(os.path.exists('../크롤링/피케_카라티셔츠/resize')==False):
    os.mkdir('../크롤링/피케_카라티셔츠/resize')
    format = [".jpg", ".png", ".jpeg", "bmp", ".JPG", ".PNG", "JPEG", "BMP"]  # 지원하는 파일 형태의 확장자들
    for (path, dirs, files) in os.walk(targetdir):
        for file in files:
            if file.endswith(tuple(format)):
                image = Image.open(path +"/"+ file)
                print(image.filename)
                print(image.size)
                image = image.resize((100,100))
                image.save('../크롤링/피케_카라티셔츠/resize/' + file)
                # image.save(file)
                print(image.size)

            else:
                print(path)
                print("InValid", file)

# 변환할 이미지 목록 불러오기
image_path = '../크롤링/피케_카라티셔츠/resize/'
img_list = os.listdir(image_path)  # 디렉토리 내 모든 파일 불러오기
img_list_jpg = [img for img in img_list if img.endswith(".jpg")]  # 지정된 확장자만 필터링

print("img_list_jpg: {}".format(img_list_jpg))

img_list_np = []

for i in img_list_jpg:
    img = Image.open(image_path + i)
    img_array = np.array(img)
    img_list_np.append(img_array)
    print(i, " 추가 완료 - 구조:", img_array.shape)  # 불러온 이미지의 차원 확인 (세로X가로X색)
    print(img_array.T.shape) #축변경 (색X가로X세로)

img_np = np.array(img_list_np)  # 리스트를 numpy로 변환
np.save('./sample_data', img_np)  # x_save.npy
print(img_np.shape)
print("결과: 정상적 으로 저장 완료")