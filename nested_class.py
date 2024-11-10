class Company:

  class Employee:
    def __init__(self,name,position):
      self.name=name
      self.position=position

    def get_details(self):
      return f"{self.name} is a {self.position}"

  def __init__(self,company_name):
    self.company_name=company_name
    self.emp_list=[]

  def add_employee(self,name,position):
    new_emp=self.Employee(name,position)
    self.emp_list.append(new_emp)

  def list_employees(self):
    return [emp.get_details() for emp in self.emp_list]

company1=Company("Krusty Crabs")

print(company1.company_name)

company1.add_employee('Anand','Business Analyst')
company1.add_employee('Vivek','Architect')
company1.add_employee('Gregor','Manager')

print(company1.list_employees())

for emp in company1.list_employees():
  print(emp)



company2=Company("Major Sir Captain Company")

print(company2.company_name)

company2.add_employee('Sheldon','VP')
company2.add_employee('Susana','Director/Assistant')

for emp in company2.list_employees():
  print(emp)