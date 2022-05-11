import csv
import os

# Get the path to the file
path=['긴팔티셔츠', '민소매티셔츠', '반팔티셔츠', '피케_카라티셔츠', '후드티셔츠']
dir_path = ['./크롤링/긴팔티셔츠', './크롤링/민소매티셔츠', './크롤링/반팔티셔츠', './크롤링/피케_카라티셔츠', './크롤링/후드티셔츠']

file = {"name":""}
for i in range(5):
    for filename in os.listdir(dir_path[i]):
        file["name"] = filename
        with open(path[i] + '_names.csv', 'a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=file.keys())
            writer.writerow(file)

