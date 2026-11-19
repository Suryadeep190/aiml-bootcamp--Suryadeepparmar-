from collections import defaultdict, namedtuple, deque, Counter
import string


# ==========================================
# TASK 1: defaultdict - Group Employees
# ==========================================

employees = [
    ("IT", "Amit"),
    ("HR", "Priya"),
    ("IT", "Rahul"),
    ("Finance", "Neha"),
    ("HR", "Karan"),
    ("Finance", "Meera"),
    ("IT", "Ravi")
]

grouped = defaultdict(list)

for department, employee in employees:
    grouped[department].append(employee)

print("\n--- DEFAULTDICT: Employee Groups ---")

for department, employee_list in grouped.items():
    print(department, ":", employee_list)


# ==========================================
# TASK 2: namedtuple - Employee Information
# ==========================================

Person = namedtuple("Person", ["name", "age", "city"])

employee_data = [
    ("Amit", 24, "Ahmedabad"),
    ("Priya", 26, "Mumbai"),
    ("Rahul", 23, "Delhi")
]

people = [Person(*employee) for employee in employee_data]

print("\n--- NAMEDTUPLE: Employee Details ---")

for p in people:
    print(f"Name: {p.name}, Age: {p.age}, City: {p.city}")

print("\nAccessing city using index:", people[0][2])
print("Accessing city using name:", people[0].city)




search_history = deque(maxlen=5)

searches = [
    "Python",
    "Machine Learning",
    "Deep Learning",
    "Data Science",
    "Artificial Intelligence",
    "Computer Vision",
    "Natural Language Processing"
]

print("\n--- DEQUE: Search History ---")

for search in searches:
    search_history.append(search)
    print("New Search:", search)
    print("History:", list(search_history))

print("\nFinal Search History:", list(search_history))



text1 = """
Python is a powerful programming language.
Python is useful for machine learning.
"""

text2 = """
Python is a popular language.
Machine learning uses Python.
"""

# Normalize text
text1 = text1.lower().translate(str.maketrans("", "", string.punctuation))
text2 = text2.lower().translate(str.maketrans("", "", string.punctuation))

# Split into words
words1 = text1.split()
words2 = text2.split()

# Count words
counter1 = Counter(words1)
counter2 = Counter(words2)

# Compare words
common_words = counter1.keys() & counter2.keys()
only_text1 = counter1.keys() - counter2.keys()
only_text2 = counter2.keys() - counter1.keys()

print("\n--- COUNTER: Text Comparison ---")

print("Common words:", sorted(common_words))
print("Only in Text 1:", sorted(only_text1))
print("Only in Text 2:", sorted(only_text2))

print("\nText 1 Frequencies:", counter1)
print("Text 2 Frequencies:", counter2)