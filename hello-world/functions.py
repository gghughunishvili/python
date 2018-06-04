students = []

def add_students(name, age, school):
    students.append({"name": name, "age": age, "school": school})

def var_args(name, *args):
    print(name)
    print(args)

def kargs(name, **kargs):
    print(name)
    print(kargs)

add_students(name="Steve", age=29, school="Unknown")
print(students)

var_args("test", "some", "other")
kargs(name="steve", age=11, id=203032)
