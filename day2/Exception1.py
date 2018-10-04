def my_func(x, y):
    print("Entering my_func()")
    if y == 0:
        raise ValueError("y can't be 0")
    z = x / y
    print("Exiting my_func()")
    return z


def main():
    try:
        result = my_func(10, 0)
    except ValueError as e:
        print(e)
    except ZeroDivisionError as e:
        print(e)
    else:
        print(result)
    finally:
        print("I'm out of here")

    print("Bye")

if __name__ == '__main__':
    main()
