from random_address import real_random_address


def get_address():
    address = real_random_address()
    return address['address1'], address['city'], address['state'], address['postalCode']


if __name__ == '__main__':
    street, city, state, postal_code = get_address()

    print('Street:', street)
    print('City:', city)
    print('State:', state)
    print('Postal code:', postal_code)
