
def add_sprinkles(func):
  def wrapper(*args,**kwargs):
    print("This is your sprinkles ✨")
    func(*args,**kwargs)

  return wrapper

def add_fudge(func):
  def wrapper(*args,**kwargs):
    print("Here is your fudge 🍫")
    func(*args,**kwargs)
  return wrapper

@add_fudge
@add_sprinkles
def get_the_ice_cream(flavor):
  print(f'Here is your {flavor} ice-cream 🍧')

get_the_ice_cream('Vanilla')