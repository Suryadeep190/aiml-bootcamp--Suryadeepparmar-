import csv
import json

print("\n CSV FILE HANDLING ")

# 1. Write data into CSV file
with open("students.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["Name", "Age", "Course"])
    writer.writerow(["Rahul", 21, "Python"])
    writer.writerow(["Priya", 22, "Data Science"])
    writer.writerow(["Amit", 20, "Java"])


# 2. Read CSV file line by line
print("\nCSV Records:")

with open("students.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:
        print(row)




print("\nJSON FILE HANDLING ")

# 1. Create Python data
students = [
    {"name": "Rahul", "age": 21, "course": "Python"},
    {"name": "Priya", "age": 22, "course": "Data Science"},
    {"name": "Amit", "age": 20, "course": "Java"}
]


# 2. Write data into JSON file
with open("students.json", "w") as file:

    json.dump(students, file, indent=4)


# 3. Read JSON file
print("\nJSON Records:")

with open("students.json", "r") as file:

    data = json.load(file)

    for student in data:
        print(student)