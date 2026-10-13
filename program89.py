"""
instance methods : rectangle area and perimeter
problem : create a rectangle class with length and breadth . use instance
methods to calculate its area and perimeter
"""
class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)
r=Rectangle(10,5)
print("Area:", r.area())
print("Perimeter:", r.perimeter())
