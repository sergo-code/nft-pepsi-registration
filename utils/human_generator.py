from utils import get_mnemonic, get_public_address, get_names, get_address, get_date_of_birth


class Human:
    def __init__(self):
        self.mnemonic = get_mnemonic()
        self.public_address = get_public_address(self.mnemonic)
        self.date_of_birth = get_date_of_birth()
        self.first_name = None
        self.last_name = None
        self.street = None
        self.city = None
        self.state = None
        self.postal_code = None
        self.email = ''
        self.password = hex(16)
        self._generator()

    def _generator(self):
        self.first_name, self.last_name = get_names()
        self.street, self.city, self.state, self.postal_code = get_address()


if __name__ == '__main__':
    h = Human()

    print(h.mnemonic)
    print(h.public_address)
    print(h.first_name)
    print(h.last_name)
    print(h.date_of_birth)
    print(h.street)
    print(h.city)
    print(h.state)
    print(h.postal_code)
    print(h.email)
    print(h.password)
