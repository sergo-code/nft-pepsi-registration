import csv

file_path = 'data/account.csv'


def csv_reader():
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            print(', '.join(row))


def csv_writer(data):
    with open(file_path, 'a') as csvfile:
        fieldnames = ['seed', 'address', 'first_name', 'last_name', 'day_of_birth', 'street', 'city', 'state']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
        writer.writerow(data)


if __name__ == '__main__':
    data = {'seed': 'renew spirit pet smoke habit road tree smoke client true horse put',
            'address': '0x0baEDc4756Cd9e8949748D',
            'first_name': 'Ivan',
            'last_name': 'Ivanov',
            'day_of_birth': '07/12/2000',
            'street': 'street_test',
            'city': 'city_test',
            'state': 'state_test'}

    csv_writer(data)
    csv_reader()
