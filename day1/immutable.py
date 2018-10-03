def main():
    x = 10
    y = x
    print(id(x))
    print(id(y))
    y += 1
    print(id(x))
    print(id(y))

    l1 = [1,2,3]
    l2 = l1
    print(id(l1))
    print(id(l2))
    l2.append(4)
    print(id(l1))
    print(id(l2))



if __name__ == '__main__':
    main()
