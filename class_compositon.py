class Engine:
  def __init__(self,horsepower):
    self.horsepower=horsepower

class Wheel:
  def __init__(self,size):
    self.size=size

class Car:
  def __init__(self,make,model,horsepower,wheel_size):
    self.make=make
    self.model=model
    self.engine=Engine(horsepower)
    self.wheels=[Wheel(wheel_size) for wheel in range(4)]

  def display_car(self):
    return print(f" {self.make} {self.model} has 4 wheels of {self.wheels[0].size} (in) and the engine power is {self.engine.horsepower} (hp) ")
  

car1=Car('Maruti', 'Baleno' , 2000 , 20 )
car2=Car('MB','S-Class',5000,45)

car1.display_car()
car2.display_car()