

def square(x):
    return x * x

s = lambda x: x * x

print(s(5))
print(square(3))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


fillter_num = filter(lambda num: num % 2, numbers)
print(list(fillter_num))

# for num in numbers:
#     print(numbers_func(num))
