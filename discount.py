amount=int(input("Enter amount"))
if amount>100 :
    discount_price=amount*(10/100)
    price=amount-discount_price
    print(price)
 
else:
    discount_price=amount*(5/100)
    price=amount-discount_price
    print(price)
    