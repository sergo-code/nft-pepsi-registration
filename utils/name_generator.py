import names


def get_names():
    return names.get_full_name(gender='male').split()


if __name__ == '__main__':
    first_name, last_name = get_names()

    print('First name:', first_name)
    print('Last name:', last_name)
