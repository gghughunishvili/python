students = []

class Student:
    school_name = "Giorgi's Private School"
    def __init__(self, name, id=101):
        self.name = name
        self.id = id
        students.append(self)

    # Object to string
    def __str__(self):
        return "Student " + self.name;

    def get_school_name(self):
        return self.school_name

student = Student("Steve")
print(student)
print(students)
print(Student.school_name)
