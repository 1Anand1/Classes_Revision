#  R(P,Q)
#  C(B) <- B(A) <- A


class Animal:
  def __init__(self,name):
    self.name=name

  def eat(self):
    print(f'{self.name} is eating')

  def sleep(self):
    print(f'{self.name} is sleeping')

class Prey(Animal):
  def flee(self):
    print(f'{self.name} is fleeing') 

  # def hunt(self):
  #   print(f'{self.name} is hunting')

class Predator(Animal):
  def hunt(self):
    print(f'{self.name} is hunting')

class Hawk(Predator):
  pass

class Rabbit(Prey):
  pass

class Fish(Prey,Predator):
  pass

fish=Fish("Nemo")
hawk=Hawk("John")
rabbit=Rabbit("Bugs")



rabbit.eat()

rabbit.sleep()

rabbit.flee()

rabbit.hunt()



hawk.eat()

hawk.sleep()

hawk.flee()

hawk.hunt()


fish.eat()

fish.sleep()

fish.flee()

fish.hunt()