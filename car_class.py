class Car:
  def __init__(self,model,year,color,for_sale):
    self.model=model
    self.year=year
    self.color=color
    self.for_sale=for_sale

  def drive(self):
    print(f'{self.model} is driving :)')

  def stop(self):
    print(f'{self.model} is bought in {self.year} & is stopping :( ')