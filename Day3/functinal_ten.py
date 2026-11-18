from functools import reduce
from itertools import chain,accumulate


def task_01(numbers):
    result = []
    for n in numbers:
        if n % 2 != 0:
            result.append(n ** 2)
    return result
def Func_01(numbers):
    return list(map(lambda n: n**2,filter(lambda n:n%2 !=0,numbers)))


def task_02(names):
    result = []
    for name in names:
        result.append(name.strip().upper())
    return result
def func_02(names):
    return list(map(lambda name:name.strip().upper(),names))


def task_03(list1, list2):
    result = []
    for i in range(len(list1)):
        result.append(list1[i] * list2[i])
    return result
def func_03(list1,list2):
    return list(map(lambda pair:pair[0]*pair[1],zip(list1,list2)))


def task_04(words):
    result = []
    for word in words:
        if len(word) > 4:
            result.append(word)
    return result
def func_04(words):
    return list(filter (lambda word:len(word)>3,words))


def task_05(numbers):
    result = 1
    for n in numbers:
        result *= n
    return result
def func_05(numbers):
    return reduce(lambda x,y:x*y,numbers,1)


def task_06(items):
    total = 0
    for item in items:
        total += item["price"]
    return total
def func_06(items):
    return sum(map(lambda item:item["price"],items))


def task_07(nested_list):
    result = []
    for sublist in nested_list:
        for item in sublist:
            result.append(item)
    return result
def func_07(nested_list):
    return list(chain.from_iterable(nested_list))


def task_08(words):
    result = {}
    for word in words:
        result[word] = len(word)
    return result
def func_08(words):
    return dict(map(lambda word:(word,len(word)),words))


def task_09(values):
    result = []
    for value in values:
        if value:
            result.append(value)
    return result
def func_09(values):
    return list(filter(None,values))


def task_10(numbers):
    result = []
    total = 0
    for n in numbers:
        total += n
        result.append(total)
    return result
def func_10(numbers):
    return list(accumulate(numbers))


if __name__ == "__main__":
    
    
    print("loop:",task_01([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print("functional:",Func_01([1, 2, 3, 4, 5, 6, 7, 8, 9]))

    print("loop:",task_02(["  Alice  ", "  Bob  ", "  Charlie  "]))     
    print("functional:",func_02(["  Alice  ", "  Bob  ", "  Charlie  "]))
    
    print("loop:",task_03([1, 2, 3], [4, 5, 6]))
    print("functional:",func_03([1, 2, 3], [4, 5, 6]))
    
    print("loop:",task_04(["apple", "banana", "cat", "grape", "pear"]))
    print("functional:",func_04(["apple", "banana", "cat", "grape", "pear"]))
    
    print("loop:",task_05([2, 4, 2, 4, 6, 4]))
    print("functional:",func_05([2,4,2,4,6,4]))
    
    print("loop:",task_06([{"name": "item1", "price": 10}, {"name": "item2", "price": 20}, {"name": "item3", "price": 30}]))
    print("functional:",func_06([{"name": "item1", "price": 10}, {"name": "item2", "price": 20}, {"name": "item3", "price": 30}]))
    
    print("loop:",task_07([[1, 2], [3, 4], [5, 6]]))
    print("functional:",func_07([[1, 2], [3, 4], [5, 6]]))
    
    print("loop:",task_08(["apple", "banana", "cat", "grape", "pear"]))
    print("functional:",func_08(["apple", "banana", "cat", "grape", "pear"]))
    
    print("loop:",task_09([0, 10, "", "Hello", None, [], 25]))
    print("functional:",func_09([0, 10, "", "Hello", None, [], 25]))
    
    print("loop:",task_10([1, 2, 3, 4, 5]))
    print("functional:",func_10([1, 2, 3, 4, 5]))
    
""" I prefer functional coding cause it reduce code length and also
makes it clean and easy to read by reducing number of loops and built in functions usage"""
