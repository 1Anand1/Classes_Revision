import math

class Shape:
  
  objects=0
  
  def __init__(self,color,is_filled):
    self.color=color
    self.is_filled=is_filled
    Shape.objects+=1

  def describe(self):
    print(f'It is an entity which is {self.color} & it is {'filled' if self.is_filled else "not filled"}')

class Circle(Shape):
  def __init__(self,color,is_filled,radius):
    super().__init__(color,is_filled)
    self.radius=radius

  def describe(self):
    super().describe()
    print(f'It is a circle with an area of {round(math.pi*self.radius*self.radius,2)} cm^2 ')

class Sqaure(Shape):
  def __init__(self,color,is_filled,width):
    super().__init__(color,is_filled)
    self.width=width

  def describe(self):
    super().describe()
    print(f'It is a square with an area of {round(self.width*self.width,2)} cm^2 ')

class Triangle(Shape):
  def __init__(self,color,is_filled,width,height):
    super().__init__(color,is_filled)
    self.width=width
    self.height=height
    
  def describe(self):
    super().describe()
    print(f'It is a triangle with an area of {round((self.height*self.width)/2,2)} cm^2 ')




triangle=Triangle(color='Red',is_filled=True,width=5,height=12)
square=Sqaure(color='Yellow',is_filled=False,width=5)
circle=Circle(color='Green',is_filled=True,radius=10)


Shape.objects

triangle.width
triangle.height
triangle.color
triangle.is_filled

circle.radius
circle.color
circle.is_filled

square.width
square.color
square.is_filled

square.describe()
circle.describe()
triangle.describe()