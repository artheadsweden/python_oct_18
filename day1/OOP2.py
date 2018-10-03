class A:
    def __init__(self):
        print("__init__A")
        self.x = 10

class B(A):
    def __init__(self):
        print("__init__B")
        super().__init__()
        self.x += 2

class C(A):
    def __init__(self):
        print("__init__C")
        super().__init__()
        self.x += 2


class D(B, C):
    def __init__(self):
        print("__init__D")
        super().__init__()
        print(self.x)


def main():
    d = D()
    print(D.mro())


if __name__ == '__main__':
    main()
