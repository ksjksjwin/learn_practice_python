class Student:
  #constructor
  def __init__(self, name, year):
    #attribute
    self.name = name
    self.year = year
    self.grades = []
  # add_grade method
  def add_grade(self, grade):
    if type(grade) is Grade:
      self.grades.append(grade)      

class Grade:
  minimum_passing = 65
  
  def __init__(self, score):
    self.score = score

#instances of the Student class    
roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)
pieter.add_grade(Grade(100))
