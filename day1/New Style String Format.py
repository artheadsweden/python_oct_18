def main():
    first_name = "Anna"
    last_name = "Jones"
    age = 34

    msg = "Hi {0}, your full name is {0} {1} and you are {2} years old".format(first_name, last_name, age)
    print(msg)

    # Align
    msg = "{:>10}".format(first_name)
    print(msg)

    # Pad
    msg = "{:10}!".format(first_name)
    print(msg)

    # Floating point format
    msg = "{:06.2f}".format(3.4565646445645)
    print(msg)

if __name__ == '__main__':
    main()
