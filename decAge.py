dec={1:{'name':'john','age':27,'sex':'male'},
     2:{'name':'marie','age':22,'sex':'female'},
     3:{'name':'sali','age':23,'sex':'female'}}

for key in dec:
    if(dec[key]['age']>22):
        print(dec[key]['name']) 
    