# 데이터 수집 및 정제 작업

## 1. 수집

- 무신사 스토어에서 티셔츠 전체를 크롤링
- 티셔츠 품명, 티셔츠 브랜드명, 티셔츠의 이미지 파일

## 2. 정제

- [품명, 브랜드명, 이미지 파일명] 튜플의 수 > [이미지 파일] 튜플의 수 문제 발생
- [품명, 브랜드명, 이미지 파일명] 튜플 중 중복된 "이미지 파일명"을 갖는 튜플 모두 제거

```py
import json
import os
import pandas as pd
import sys

# Get the path to the file
path = ['./긴팔티셔츠.json', './민소매티셔츠.json', './반팔티셔츠.json', './피케_카라티셔츠.json', './후드티셔츠.json']

for i in path:
    # Get the file
    with open(i, 'r', encoding="utf-8") as f:
        data = json.load(f)
    df = pd.json_normalize(data['info'])    # Delete duplicate data
    df2 = df.drop_duplicates(subset=['product_num'])
    df2 = df2.drop_duplicates(subset=['product_img'])
    # Save the file
    df2.to_csv(i.replace('json', 'csv'), index=False)
```

- [이미지 파일]의 이름과 일치하지 않는 [이미지 파일명]갖는 튜플들 모두 제거

```sh
# brew install jq
# .json에서의 [이미지 파일명]과 일치하는 [이미지 파일]이 없는 경우를 찾아냄  

cat 파일명.json | jq '.[]' | jq '.["product_img"]' | while read line; do
        line=${line: (1):(-1)}
        if [[ -z "$(find ../PICS/폴더명/ -name "*${line}")" ]]; then
                echo DUP : $line >> 폴더명-non.out
        else
		    echo NON-DUP : $line
	fi
done
```
