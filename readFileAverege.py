file=open("readfromfile.txt","r")
count=0
sum_=0
for line in file:
    sum_+=float(line)
    count+=1
print(sum_/count)
