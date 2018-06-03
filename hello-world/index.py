# IF statements
a = 1
b = 2
print("bigger" if a > b else "smaller")

# Lists
student_names = ["Giorgi", "Jake", "Jenny", "Jessy", "Jason"]
student_names.append("Mark")
print(student_names[-3])
print("Giorgi" in student_names)
del student_names[1]
print("Jake" not in student_names)
print(student_names)
print(student_names[1:])
print(student_names[1:-2])
for name in student_names:
    print(f"Loops student_names: {name}")
    print("With another formatter: {0}".format(name))

for index in range(100, 200, 17):
    print("Index looping: {0}".format(index))