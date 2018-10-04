def func(a):
    return a**2


def main():
    numbers = [1, 2, 3, 4]
    result = list(map(func, numbers))
    print(result)

    result = list(map(lambda a: a**2, numbers))
    print(result)

    result = [number**2 for number in numbers]
    print(result)

if __name__ == '__main__':
    main()
