def ff(x, y):
    return x + y

def main():
    f = lambda x, y: x + y
    print(f(3, 4))
    print(ff(3, 4))
    result = (lambda x, y: x + y)(4, 5)
    print(result)


if __name__ == '__main__':
    main()
