from abc import ABC,abstractmethod
import math

class Shape(ABC):

  @abstractmethod
  def area(self):
    pass

class Circle(Shape):

  def __init__(self,radius):
    self.radius=radius

  def area(self):
    return round(math.pi*self.radius**2,2)

class Triangle(Shape):

  def __init__(self,base,height):
    self.base=base
    self.height=height
  
  def area(self):
    return round(self.height*self.base*0.5,2)


class Square(Shape):

  def __init__(self,side):
    self.side=side

  def area(self):
    return round(self.side**2,2)
  
class Pizza(Circle):
  def __init__(self,radius,topping):
    super().__init__(radius)
    self.topping=topping

  def area(self):
    print(f'Hey I have got a {self.topping} pizza')
    return super().area() # Each function must return something :)

shapes=[Circle(10),Triangle(2,8),Square(15),Pizza(100,"Chilli")]

for shape in shapes:
  print(f'{shape.area()} cm\u00b2') #\u00b2 is used to make the 2 as super script

