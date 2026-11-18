def fib_list(n):
    result = []

    a, b = 0, 1

    for i in range(n):
        result.append(a)
        a, b = b, a + b

    return result


def fib_gen(n):

    a, b = 0, 1

    for i in range(n):
        yield a
        a, b = b, a + b


print("Fibonacci using normal function:")
print(fib_list(10))

print("\nFibonacci using generator:")
print(list(fib_gen(10)))


print("\nChecking return types:")

print(type(fib_list(10)))
print(type(fib_gen(10)))


print("\nLooping over the same generator twice:")

my_generator = fib_gen(10)

print("First loop:")
for number in my_generator:
    print(number)

print("Second loop:")
for number in my_generator:
    print(number)

"""The second loop does not print anything because the generator has already been used
in the first loop.It can only be iterated over once.for iterating again we need to make a
new iterator object to call generator function again  """