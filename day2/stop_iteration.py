def main():
    values = (x for x in [1,2,3])
    print(next(values))
    print(next(values))
    print(next(values))
    print(next(values))


if __name__ == '__main__':
    main()
