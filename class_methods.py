from typing import Optional
class Student:

  count=0
  total_gpa=0


  def __init__(self,
               name:str,
               gpa:Optional[float]):
    self.name=name
    self.gpa=gpa
    Student.count+=1
    Student.total_gpa+=gpa

  def get_info(self):
    return f"{self.name} has scored {self.gpa}"
  
  @classmethod
  def count_student(cls):
    return f"The class has total {cls.count} students"

  @classmethod
  def average_gpa(cls):
    return f"The average GPA of the class is {cls.total_gpa/cls.count:.2f}"


student1=Student('Spongebob',3.2)
student2=Student('Sandy',2.0)
student3=Student('Matthieu',4.0)

Student.count_student()
Student.average_gpa()
