class Rectangle:


  def __init__(self,height,width):
    self._height=height
    self._width=width


  @property
  def width(self):
    return f"{self._width:.1f} cm"

  @property
  def height(self):
    return f"{self._height:.1f} cm"

  @width.setter
  def width(self,new_width):
    if new_width>0:
      self._width=new_width
    else:
      print(f'The width should always be greater than zero but the width that you provided is {new_width}')

  @height.setter
  def height(self,new_height):
    if new_height>0:
      self._height=new_height
    else:
      print(f'The height should always be greater than zero but the height you provided is {new_height}')

  @height.deleter
  def height(self):
    del self._height
    print('Well !! Height was deleted !!')

  @width.deleter
  def width(self):
    del self._width
    print('Well Okay ! Width is deleted now !!!')

rectangle=Rectangle(3,5)

rectangle.height=-1

rectangle.width=0

print(rectangle.height)

print(rectangle.width)

print(rectangle._height)

print(rectangle._width)

rectangle.height=10

rectangle.width=100

print(rectangle.height)

print(rectangle.width)

rectangle1=Rectangle(-3,-5)

print(rectangle1.height)

print(rectangle1.width)

del rectangle1.height

del rectangle1.width

print(rectangle1.height)

print(rectangle1.width)
