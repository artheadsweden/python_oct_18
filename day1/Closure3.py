# LEGB

x = 10

def outer():
    y = 12
    def inner():
        y = 30
        print(x)
        print(y)

    return inner


def func1():
    print(x)

def main():
    global x
    print(x)
    x += 1
    func1()
    f = outer()
    f()
    f()
    f1 = outer()
    f1()


if __name__ == '__main__':
    main()
