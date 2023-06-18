import json
import random
import string
import sys


def load_db(filename='users_db.json'):
    with open(filename, 'r') as file:
        db = json.load(file)
        return db


def save_db(db, filename='users_db.json'):
    with open(filename, 'w') as file:
        json.dump(db, file, indent=2)
    print(f'File "{filename}" saved successfully')


db = load_db()
'''Список из словарей'''


def print_db(db):  # Распечатка внутренностей библиотеки
    print(f"{len(db)} users found:")
    for i in range(0, len(db)):
        print(f"Username: {db[i]['login']:10} |Password: {db[i]['password']:15} | Site:,{db[i]['site']:30} |")


def add_user(db):
    site = input('Новая запись.\nВведите имя сайта (enter to cancel):  ')
    if not site:
        return print('you canceled new input')
    else:
        login = input('Введите логин:  ')
        password = input('Введите пароль:  ')
        db.append({
            'login': login,
            'password': password,
            'site': site
        })
    save_db(db)


def change(subject, prev):
    new_value = input(f"input {subject}, ({prev}):    ")
    if new_value == '':
        return prev
    else:
        return new_value


def password_generator(length):
    passw = string.ascii_letters + string.digits + string.digits  # +string.punctuation
    mypass = ''
    for i in range(length):
        mypass += (random.choice(passw))
    print('New password is:\t', mypass)
    return mypass


def change_data(diff_record):
    print("Changing user's record   >>>>>>>>>>>>>>>>>>>>>>>>>")
    diff_record['site'] = change('Site name: ', diff_record['site'])
    diff_record['login'] = change('login: ', diff_record['login'])
    length = input(
        "Do you want me to generate your password?: \n(Enter length of password, Press Enter if you want to create the password manually):  ")
    if not length:
        diff_record['password'] = change('password: ', diff_record['password'])
    else:
        diff_record['password'] = password_generator(int(length))
    save_db(db)


def choose_user_to_change(db):  # Распечатать пользователей из базы
    for i in range(0, len(db)):
        print(i, 'User:', db[i]['login'])
    number_to_change = int(input('Choose user number to change: '))
    user_to_change = db[number_to_change]['login']
    for i in range(0, len(db)):
        if user_to_change == db[i]['login']:
            print('You chose user:', db[i]['login'])
            return i


# choose_user_to_change(db)
# add_user(db)
# print(db)
def search(db):
    user = input('Enter username to find:\t')
    for items in db:
        if user == items['login']:
            responce = f"\nFound:\nUser: {user:10} | password: {items['password']:10} | site: {items['site']}"
            return responce
    responce = f'\nUser: {user} not found.'
    return responce


def remove_user(db):
    user_to_del = choose_user_to_change(db)
    print(f"'{db[user_to_del]['login']}' has been removed")
    del db[user_to_del]
    save_changes = input("Save changes? y/N     ")
    match save_changes.lower():
        case 'y':
            save_db(db)
        case _:
            print('Changes cancelled')


def main_menu():
    print("____________________________\nUsers's data operations >>>>")
    choice = (input('Add a new user = 1\n'
                    'Change user data = 2\n'
                    'Print all users data = 3\n'
                    'Find user by name = 4\n'
                    'Remove user = 5\n'
                    'Exit = 0\n'
                    '---------------------------\n'
                    'Enter the number of action:\t'))
    # if choice == 1:
    #     add_user(db)
    # elif choice == 2:
    #     choose_user_to_change(db)
    # elif choice == 3:
    #     print_db(db)
    # elif choice == 4:
    #     print(search(db))
    # elif choice == 0:
    #     sys.exit('Goodby')

    match choice:
        case '1':
            add_user(db)
        case '2':
            i = choose_user_to_change(db)
            change_data(db[i])
        case '3':
            print_db(db)
        case '4':
            print(search(db))
        case '5':
            remove_user(db)
        case '0':
            sys.exit('Goodbye!')
        case _:
            print('Wrong input!')


while True:
    main_menu()

# *****************************************************
# db = [
#   {
#     "login": "admin",
#     "password": "1234",
#     "site": "www.some.ru"
#   },
#   {
#     "login": "User",
#     "password": "222",
#     "site": "www.site.net"
#   },
#   {
#     "login": "vovik",
#     "password": "3333",
#     "site": "www.vovik.net"
#   }
# ]
