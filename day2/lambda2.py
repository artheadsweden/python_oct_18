def my_func(func, x, y):
    print(func(x, y))

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def main():
    my_func(lambda a, b: a + b, 5, 3)
    my_func(lambda a, b: a - b, 5, 3)

    my_func(add, 5, 3)
    my_func(sub, 5, 3)

if __name__ == '__main__':
    main()
