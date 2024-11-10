class Animal:
  is_alive=True

class Dog(Animal):
  def speak(self):
    print("WOOF!!")

class Cat(Animal):
  def speak(self):
    print("MEOW!!")

class Car:
  is_alive=True

  def speak(self):
    print("HONK!!")


animals=[Dog(),Cat(),Car()]

for animal in animals:
  animal.speak()
  animal.is_alive