class MyStudentClass:

  year=2024
  count_of_students=0


  def __init__(self,name,marks):
    self.name=name
    self.marks=marks
    MyStudentClass.count_of_students+=1


