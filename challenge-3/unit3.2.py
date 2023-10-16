class Student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_students(student_list):
  sorted_students = sorted(student_list,
                           key=lambda student: student.cgpa,
                           reverse=True)
  return sorted_students


students = [
    Student("Akilan", "A123", 6.1),
    Student("Bharath", "A124", 8.3),
    Student("Ira", "A125", 9.7),
    Student("San", "A126", 9.9),
]

sorted_students = sort_students(students)

for student in sorted_students:
  print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name,
                                                     student.roll_number,
                                                     student.cgpa))