students = {
    "Ben": 1,
    "Jan": 2,
    "Peter": 1,
    "Melissa": 4
}
print(students)

# Read element
student1 = students["Ben"]
print(student1)

# Update element
students["Ben"] = 6
print(students)

# Add element 1
students["Julia"] = 1
# Add element 2 / update element 2
students.update({"Chris": 1})
print(students)

# Remove element
students.pop("Julia")
print(students)

# Iterate over keys
for student in students:
    print(student)

# Iterate over values
for grade in students.values():
    print(grade)

# Iterate over keys and values
for key, value in students.items():
    print(key, value)
