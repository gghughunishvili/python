students = []

class Student:
    def add(self, name, id=101):
        student = {"name": name, 'id': id}
        students.append(student)

student = Student()
student.add("Steve")
print(students)
