from functools import reduce

def func(a, b):
    return a * b

def largest(a, b):
    return a if a > b else b

def main():
    numbers = [1, 22, 3, 4]
    result = reduce(func, numbers)
    print(result)

    result = reduce(lambda a, b: a * b, numbers)
    print(result)

    result = reduce(largest, numbers)
    print(result)

    result = reduce(lambda a, b: a if a > b else b, numbers)
    print(result)


if __name__ == '__main__':
    main()
