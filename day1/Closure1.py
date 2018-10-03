
def outer(name):
    def inner(age):
        return f"Hi {name}, I see you are {age} years old"
    return inner


def main():
    f = outer("Paul")
    result = f(45)
    print(result)

    f1 = outer("Anna")
    result = f1(34)
    print(result)

    result = f(22)
    print(result)


if __name__ == '__main__':
    main()
