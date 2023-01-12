from random import randint


def get_date_of_birth():
    day = randint(1, 28)
    month = randint(1, 12)
    year = randint(1990, 2002)

    day = day if day >= 10 else f'0{day}'
    month = month if month >= 10 else f'0{month}'

    return f'{day}/{month}/{year}'


if __name__ == '__main__':
    date_of_birth = get_date_of_birth()

    print(date_of_birth)
