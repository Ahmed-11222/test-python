i=int(input("choose 1 for triangle. 2 for square. 3 for circle and 4 for cylinder "))

def triangle_area(t_base, t_height):
    t_area=(t_base/t_height)
    print(t_area)
    
def square_area(s_length, s_width):
    s_area=(s_length/s_width)
    print(s_area)
    
def cylinder_area(cylinder_length, cylinder_width):
    cylinder_area=(cylinder_length/cylinder_width)
    print(cylinder_area)
    

def circle_area(circle_radius, pi):
    circle_area=(circle_radius*pi)
    print(circle_area)

    
if (i==1):
        t_base=int(input("triangle base"))
        t_height=int(input("triangle height"))
        triangle_area(t_base, t_height)
        
elif (i==2):
         s_length=int(input("square length"))
         s_width=int(input("square width"))
         square_area(s_length, s_width)
         
elif (i==3):
         circle_radius=float(input("circle radius"))
         pi=3.14
         circle_area(circle_radius, pi)
         
elif (i==4):
         cylinder_radius=float(input("cylinder radius"))
         cylinder_height=int(input("cylinder length"))
         cylinder_area(cylinder_radius, cylinder_height)
         
         
         
