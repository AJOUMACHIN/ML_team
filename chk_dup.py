import json
import os
import pandas as pd
import csv
import sys

# Get the path to the file
path = ['./긴팔티셔츠.csv', './민소매티셔츠.csv', './반팔티셔츠.csv', './피케_카라티셔츠.csv', './후드티셔츠.csv']
dir_path = ['./크롤링/긴팔티셔츠', './크롤링/민소매티셔츠', './크롤링/반팔티셔츠', './크롤링/피케_카라티셔츠', './크롤링/후드티셔츠']
# Get the file name
for i in path:
    cnt=0
    ohmycnt=0
    # Get the file
    data = pd.read_csv(i)
    # Delete the wrong data
    for j in range(len(data)):
        not_exist = 1
        for filename in os.listdir(dir_path[path.index(i)]):
            if data['product_img'][j] == filename:
                not_exist = 0
                print(i+filename+"살앗다")
                cnt+=1
                break
        if not_exist == 1:
            print("---------------------------\n----------------------------\n---------------------------\n----------------------------\n---------------------------\n----------------------------")
            ohmycnt+=1
            data = data.drop(j)

    print("아이고cnt"+str(ohmycnt))
    # Save the file
    data.to_csv(i, index=False)