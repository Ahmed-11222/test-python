try:
    answer='abaacb'

    a=input("write your answers ")

    grade=0

    for i in range (len(answer)):
        if (answer[i]==a[i]):
            grade+=1
    print(grade)





except Exception as exc:
    print(type(exc))


        

    
   
    