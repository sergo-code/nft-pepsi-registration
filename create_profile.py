from utils import Human, csv_writer


def create():
    human = Human()
    data = {'seed': human.mnemonic,
            'address': human.public_address,
            'first_name': human.first_name,
            'last_name': human.last_name,
            'day_of_birth': human.date_of_birth,
            'street': human.street,
            'city':  human.city,
            'state': human.state,
            'email': human.email,
            'password': human.password
    }
    csv_writer(data)


if __name__ == '__main__':
    create()
