import functools


# p.1 of the home task
# import os
# print(list(filter(lambda file_name: os.path.splitext(file_name)[1] == '.txt', os.listdir('../'))))


string = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in
voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident,
sunt in culpa qui officia deserunt mollit anim id est laborum.
"""

arr = string.split()


# p.2.a)
def to_lower_case():
    return lambda word: word.lower()


def to_upper_case():
    return lambda word: word.upper()


def reverse_string():
    return lambda word: word[::-1]


for w in arr:
    print(to_lower_case()(w))
    print(to_upper_case()(w))
    print(reverse_string()(w))


# p.2.b)
print(list(filter(lambda x: len(x) < 5, arr)))
print(list(filter(lambda x: x[0].upper() == 'L', arr)))
print(list(filter(lambda x: x[-1].lower() == 'e', arr)))


# p.2.c)
print(list(map(lambda x: x.capitalize(), arr)))
print(list(map(lambda x: x * 2, arr)))
print(list(map(lambda x: x[0].lower(), arr)))


# p.3
def benchmark(iterations):
    def actual_decorator(func):
        import time

        def wrapper(*args, **kwargs):
            total = 0
            for i in range(iterations):
                start = time.time()
                return_value = func(*args, **kwargs)
                end = time.time()
                total = total + (end - start)
            print(f'[*] Execution time of {func.__name__} is: {total / iterations} sec.')
            return return_value

        return wrapper

    return actual_decorator


@benchmark(iterations=1000000)
def factorial_1(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact


@benchmark(iterations=1000000)
def factorial_2(n):
    if n == 1:
        return n
    else:
        return functools.reduce(lambda x, y: x * y, range(2, n + 1))


print(factorial_1(5))
print(factorial_2(5))
