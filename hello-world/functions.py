students = []

def add_student(name, age=0):
    students.append({"name": name, "age": age})

def var_args(name, *args):
    print(name)
    print(args)

def kargs(name, **kargs):
    print(name)
    print(kargs)

# Files
def save_file(student):
    try:
        f = open("students.txt", "a")
        f.write(student + "\n")
        f.close()
    except Exception as e:
        print(e)

def read_file():
    try:
        f = open("students.txt", "r")
        for student in f.readlines():
            add_student(student)
        f.close()
    except Exception as e:
        print(e)



add_student(name="Steve", age=29)
print(students)

var_args("test", "some", "other")
kargs(name="steve", age=11, id=203032)

# Inputs
read_file()
print(students)
student_name = input("Enter student name:")
student_age = input("Enter student age:")
add_student(student_name, student_age)
print(students)
save_file(student_name)

# Lambda Functions
double = lambda x: x * 2
num_to_double = int(input("Enter a number to double:"))
print(double(num_to_double))
