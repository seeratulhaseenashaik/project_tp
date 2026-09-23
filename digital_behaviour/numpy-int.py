import numpy as np

insta_list=[]

study_time=[]

with open("digital_behaviour.csv","r",encoding:"utf-8") as f:
  reader=csv.DictReader(f)
  for row in reader:
    insta_list.append(row[APP])
    study_time.append(row["Study Time"])

insta_list=insta_list[:7]
study_time=[:7]
insta_array=np.array(insta_list)
study_array=np.array(study_time)

total=insta_array.sum()
