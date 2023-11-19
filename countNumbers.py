message=input("enter text  ")
counter=0

for i in message:
    if (i.isdigit()):
        counter+=1
print(counter)