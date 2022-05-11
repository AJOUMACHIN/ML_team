import csv
import os
import pandas as pd

# Get the path to the file
csv_path=['./긴팔티셔츠.csv', './민소매티셔츠.csv', './반팔티셔츠.csv', './피케_카라티셔츠.csv', './후드티셔츠.csv']
dir_path = ['./크롤링/긴팔티셔츠', './크롤링/민소매티셔츠', './크롤링/반팔티셔츠', './크롤링/피케_카라티셔츠', './크롤링/후드티셔츠']

for i in csv_path:
    cnt=0
    ohmycnt=0
    # Get the file
    data = pd.read_csv(i)
    for filename in os.listdir(dir_path[csv_path.index(i)]):
        not_exist = 1
        for j in range(len(data)):
            if data['product_img'][j] == filename:
                not_exist = 0
                break
        if not_exist:
            ohmycnt += 1
            os.remove(dir_path[csv_path.index(i)] + '/' + filename)
            print(filename + ' is removed')
        cnt += 1
    print(i + ' is done')
    print('Total ' + str(cnt) + ' pictures')
    print('Deleted ' + str(ohmycnt) + ' pictures')
    print('\n')
