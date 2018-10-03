def main():
    first_name = "Anna"
    last_name = "Jones"
    age = 34
    x = 1222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222

    msg = f"Hi {first_name}, your full name is {first_name} {last_name} and you are {age} years old"
    print(msg)

    # Align
    msg = f"{first_name:>10}"
    print(msg)

    # Pad
    msg = f"{first_name:10}!"
    print(msg)

    # Floating point format
    msg = f"{3.4565646445645:06.2f}"
    print(msg)


if __name__ == '__main__':
    main()
