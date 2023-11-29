class Math:
    @staticmethod
    def add_numbers(x,y):
        return x+y
        
        
    @staticmethod
    def pi():
        return 3.14
class Shape:
    def __init__(self, name, color,r):
        self.name=name
        self.color=color
    def area(self, r):
        return 2*Math.pi()*r
sh1=Shape("c1","Red", 4)

print(Math.add_numbers(3,5))