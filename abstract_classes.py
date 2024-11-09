from abc import ABC,abstractmethod

class Vehicle(ABC):

  @abstractmethod
  def go(self):
    pass

  @abstractmethod
  def stop(self):
    pass

class Car(Vehicle):
  
  def go(self):
    print('My car is driving')

  def stop(self):
    print('My car is stopping')


class MotorCycle(Vehicle):
  def go(self):
    print('I am driving my motorcycle')

  def stop(self):
    print('I am stopping my motorcycle')


class Boat(Vehicle):
  def go(self):
    print("I am sailing in my boat")

  def stop(self):
    print('I am anchoring my boat!')

car=Car()
motorcycle=MotorCycle()
boat=Boat()

car.go()
car.stop()
motorcycle.stop()
motorcycle.go()
boat.go()
boat.stop()