class Employee:
  def __init__(self,name,position):
    self.name=name
    self.position=position

  def info_display(self):
    return print(f"{self.name} is {self.position} in one company")
  
  @staticmethod

  def is_valid_position(position):
    list_of_valid_positions=['Manager','Director','Design Engineer','VP']
    return print(position in  list_of_valid_positions)
  
emp1=Employee("Umesh",'Design Engineer')
emp2=Employee('Mahesh','Manager')
emp3=Employee('Suraj','VP')

emp1.info_display()
emp2.info_display()
emp3.info_display()

Employee.is_valid_position('VP')

Employee.is_valid_position('EVP')
