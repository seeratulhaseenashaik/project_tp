import csv
APP="instagram"#fixed value

minutes=[]

with open("digital_behaviour.csv","r",encoding="utf-8") as f:
   reader=csv.DictReader(f) #reads data in dictionary format. Key values are the header values. the row values are the number of values in the dictionary
   for row in reader:
      minutes.append(int(row['Instagram_Minutes']))#all 30 values of Instagram minutes are stored in minutes

#minutes[start:stop:step] start:start index(default-0), stop:end index(not considered), step:values to jump
minutes[ :7]

total=sum(minutes)

avg=total/len(minutes)# float division
#avg=total//len(minutes) floor division
highest=max(minutes)
low=min(minutes)
count=0
for i in minutes:
   if i>avg :
      count+=1
   
print(f"\nApp: {APP} \nTotal Minutes     : {total}  \n Average Minutes   : {avg:.1f}\n Highest Day       : {highest}  \nLowest Day        : {low} \nDays Above Avg    : {count}")


   

