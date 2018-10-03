def func1(a: int, b: str, c: bool)->int:

    print(a, b, c)
    return a + 1


def main():
    name: str = "Hi"
    name = 34
    print(type(name))
    func1(1, "3.4", False)


if __name__ == '__main__':
    main()
