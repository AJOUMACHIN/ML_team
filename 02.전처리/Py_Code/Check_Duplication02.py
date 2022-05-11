import json
import os
import sys

# Get the path to the file
path = ['./긴팔티셔츠.json', './민소매티셔츠.json', './반팔티셔츠.json', './피케_카라티셔츠.json', './후드티셔츠.json']
dir_path = ['./크롤링/긴팔티셔츠', './크롤링/민소매티셔츠', './크롤링/반팔티셔츠', './크롤링/피케_카라티셔츠', './크롤링/후드티셔츠']
# Get the file name
for i in path:
    cnt=0
    ohmycnt=0
    # Get the file
    with open(i, 'r', encoding="utf-8") as f:
        data = json.load(f)
    # Delete the wrong datap
    for j in data['info']:
        not_exist = 1
        for filename in os.listdir(dir_path[path.index(i)]):
            if j['product_img'] == filename:
                not_exist = 0
                print(i+filename+"살앗다")
                cnt+=1
                break
        if not_exist == 1:
            print("아이고")
            ohmycnt+=1
            data['info'].remove(j)
    data['total']=cnt
    print("아이고cnt"+str(ohmycnt))
    # save the file
    with open(i, 'w', encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent="\t")