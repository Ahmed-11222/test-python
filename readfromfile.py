file=open("readfromfile.txt","r")
line=file.readline()
print(line)
while(line !=""):
    line=file.readline()
    print(line)