class Prey:
  def flee(self):
    print('This Animal is fleeing')

class Predator:
  def hunt(self):
    print('This Animal is hunting')

class Rabbit(Prey):
  pass

class Hawk(Predator):
  pass

class Fish(Predator,Prey):
  pass


fish=Fish()
hawk=Hawk()
rabbit=Rabbit()

fish.flee()
fish.hunt()

rabbit.flee()
hawk.hunt()