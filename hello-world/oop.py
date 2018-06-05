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

    def get_name(self):
        return self.name

    def show_me(self):
        return "I am in Student class"

student = Student("Steve")
print(student)
print(students)
print(Student.school_name)


class HighSchoolStudent(Student):
    school_name = "Giorgi's High School"

    def show_me(self):
        parent_show = super().show_me()
        return parent_show + "-- Plus additional--HSS"

giorgi = HighSchoolStudent("Giorgi")
print(giorgi.show_me())

