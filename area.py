from math import tan, pi
n=5
s=6.5
def area(n, s):
    area=(n*s**2)/4*tan(pi/n)
    print(area)
        
area(n, s)