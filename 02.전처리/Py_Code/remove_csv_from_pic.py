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
    for j in range(len(data)):
        # Get the path to the file
        path = dir_path[csv_path.index(i)]
        # Get the file name
        file_name = data['product_img'][j]
        # get the file path
        file_path = path + '/' + file_name
        if os.path.isfile(file_path):
            continue
        else:
            ohmycnt += 1
            data.drop(j, inplace=True)
        cnt += 1

    data.to_csv(i, index=False)
    print(i + ' is done')
    print('Total ' + str(cnt) + ' pictures')
    print('Deleted ' + str(ohmycnt) + ' pictures')
    print('\n')
