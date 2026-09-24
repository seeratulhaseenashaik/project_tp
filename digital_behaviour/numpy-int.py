import numpy as np
import csv

insta_list=[]

study_time=[]
APP="instagram"
with open("digital_behaviour.csv","r",encoding="utf-8") as f:
  reader=csv.DictReader(f)
  for row in reader:
    insta_list.append(int(row["Instagram_Minutes"]))
    study_time.append(int(row["Study_Minutes"]))

insta_list=insta_list[:7]
study_time=study_time[:7]
insta_array=np.array(insta_list)
study_array=np.array(study_time)

total=insta_array.sum()
avg=insta_array.mean()
maxi=insta_array.max()
mini=insta_array.min()
insta_array[0]
insta_array[-1]
insta_array[0:3]
insta_array[-2::]#to print last two values
insta_array[1:4]
#insta_array=[val/60 for val in insta_array] -> python bit which divides the value of insta_array by 60
hours=insta_array/60
diff=insta_array-study_array
greater_than_100=insta_array[insta_array>100]
count=(insta_array>100).sum()
greater=insta_array[insta_array>avg]
print(f"\nApp: {APP} \nTotal Minutes     : {total}  \n Average Minutes   : {avg:.1f}\n Highest Day       : {maxi}  \nLowest Day        : {mini} \nDays Above Avg    : {greater} \n Greater than 100: {greater_than_100}\nHours:{hours} \nDifference:{diff}")