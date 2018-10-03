def main():
    first_name = "Anna"
    last_name = "Jones"
    age = 34

    msg = "Hi %s, your full name is %s %s and you are %d years old" % (first_name, first_name, last_name, age)
    print(msg)

    # Align
    msg = "%10s" % (first_name,)
    print(msg)

    # Padding
    msg = "%-10s!" % (first_name,)
    print(msg)

    # Format floating point numbers
    msg = "%06.2f" % (3.456234234343,)
    print(msg)



if __name__ == '__main__':
    main()
