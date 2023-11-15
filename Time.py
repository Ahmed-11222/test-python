time1=int (input("enter time "))
amorpm1=input("am or pm")
time2=int (input("enter time "))
amorpm2=input("am or pm")

if amorpm1.lower()=="am" and amorpm2.lower()=="pm":
    print (time1,"",amorpm1)
elif amorpm1.lower()=="pm" and amorpm2.lower()=="am":
    print (time2, "",amorpm2)
    
else:
    if time1>time2:
        print(time2,amorpm2)
    elif time2>time1:
        print(time1, amorpm1)


