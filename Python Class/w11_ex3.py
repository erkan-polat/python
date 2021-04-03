import math
class Circle():
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        print("Area of circle is : " + str((self.radius**2)*math.pi))
    def perimeter(self):
        print("Perimeter of circle is: " + str(2*math.pi*self.radius))
              
