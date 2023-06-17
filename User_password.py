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
def print_db(db): # Распечатка внутренностей библиотеки
    print('Users"s data')
    for i in range(0, len(db)):
        print('Username:',db[i]['login'],end='; ')
        print('Password:',db[i]['password'],end='; ')
        print('Site:',db[i]['site'])

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
        "Do you want me to generate your password?: \n(Enter length of password, press Enter if you want to create the password manually):  ")
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
            print('You choode user:', db[i]['login'])
            change_data(db[i])


def main_menu():
    print("\nUsers's data operations >>>>>>>>>>>>>>>>>>>>>>>>>>" )
    choice=int(input('Add a new user = 1\n'
                     'Change user data = 2\n'
                     'Print all users data = 3\n'
                     'Exit = 0\n'
                     '---------------------------\n'
                     'Enter the number of action:\t'))
    if choice==1:
        add_user(db)
    elif choice==2:
        choose_user_to_change(db)
    elif choice==3:
        print_db(db)
    elif choice==0:
        sys.exit('Goodby')

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
