def class_average(students, passing=40):

    total = 0
    passed = 0

    for s in students:

        breakpoint()  
        total += s["marks"]
        
        if s["marks"] >= passing:
            passed += 1

    average = total / len(students)
    pass_rate = passed / len(students) * 100

    return average, pass_rate


data = [
    {"name": "asha", "marks": 88},
    {"name": "ravi", "marks": 92},
    {"name": "meera", "marks": 79},
    {"name": "dev", "marks": 40},
]

avg, rate = class_average(data)

print(f"average: {avg}")
print(f"pass rate: {rate}%")