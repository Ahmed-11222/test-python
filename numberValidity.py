n="+968 9621-1222"
valid=len(n)==14
position=0

while valid and position < len(n):
    valid=(n[5:0]=="+968 " and n[5:9].isdigit() and n[9]=="-" and n[10:15].isdigit())
    position+=1

if(valid):
    print("The number is correct")
else:
    print("the number is wrong")