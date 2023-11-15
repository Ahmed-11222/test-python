total_Amount=1000
pin=1234
write_Pin=int (input("write the pin number "))

if write_Pin==1234:
     choose=int (input("Select 1 to see total amount and 2 to deposit and 3 to withdraw "))

     if choose==1:
         
        print("your amount is: ", total_Amount)
     elif choose==2:
         
           deposit=float (input ("How much do you want to deposit "))
           price=total_Amount+deposit
           print ("your amount is ", price)
           
     elif choose==3:
         withdraw=float (input ("How much do you want to withdraw "))
         price1=total_Amount-withdraw
         print ("your amount is ", price1)
           
   
   
   