def list_add(name, name_list=None):
    if name_list is None:
        name_list = []
    name_list.append(name)
    return name_list


def main():
    my_list = []
    my_list = list_add("Anna", my_list)
    my_list = list_add("Peter", my_list)

    print(my_list)

    my_list2 = list_add("John")
    print(my_list2)

    my_list3 = list_add("Sara")
    print(my_list3)

    my_list4 = list_add("Sue")
    print(my_list4)

if __name__ == '__main__':
    main()
