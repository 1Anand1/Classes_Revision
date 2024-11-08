class Animal:
  def __init__(self,name):
    self.name=name  
    self.is_alive=True

  def eat(self):
    print(f'{self.name} is eating.')
  
  def sleep(self):
    print(f'{self.name} is asleep , do not disturb him . He will bite .')


class Dog(Animal):
  def speak(self):
    print('WOOF!!')

class Cat(Animal):
  def speak(self):
    print('MEOW!!')

class Mouse(Animal):
  def speak(self):
    print('SQEEK!!')


dog=Dog('Scooby')
cat=Cat('Tom')
mouse=Mouse('Jerry')

print(mouse.name)

print(cat.name)

print(dog.name)

print(cat.is_alive)

cat.sleep()

dog.eat()

dog.speak()
cat.speak()
mouse.speak()