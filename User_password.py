import json
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


def change_data(diff_record):
    print("Changing user's record>>>>>>>>>>>>>>>>>>>>>>>>>")
    diff_record['site'] = change('Site name: ', diff_record['site'])
    diff_record['login'] = change('login: ', diff_record['login'])
    diff_record['password'] = change('password: ', diff_record['password'])
    save_db(db)



def choose_user_to_change(db): #Распечатать пользователей из базы
    for i in range(0, len(db)):
        print(i,'User:',db[i]['login'])
    number_to_change=int(input('Choose user number to change: '))
    user_to_change=db[number_to_change]['login']
    for i in range(0, len(db)):
        if user_to_change==db[i]['login']:
            print('You choode user:', db[i]['login'])
            change_data(db[i])



        # print(db[i]['password'], end=', site: ')  '''Распечатка внутренностей библиотеки '''
        # print(db[i]['site'])


choose_user_to_change(db)
# add_user(db)
# print(db)

def password_generator():
    pass

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
