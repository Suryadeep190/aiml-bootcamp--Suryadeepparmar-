numbers = [1, 2, 3]
iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))

try:
    print(next(iterator))
except StopIteration:
    print("Error caught: StopIteration")


for x in numbers:
    print(x)


my_iterator = iter([1, 2, 3])

while True:
    try:
        x = next(my_iterator)
        print(x)
    except StopIteration:
        break

