
# заготовка для домашней работы
# прочитайте про glob.glob
# https://docs.python.org/3/library/glob.html

# Задание
# мне нужно отыскать файл среди десятков других
# я знаю некоторые части этого файла (на память или из другого источника)
# я ищу только среди .sql файлов
# 1. программа ожидает строку, которую будет искать (input())
# после того, как строка введена, программа ищет её во всех файлах
# выводит список найденных файлов построчно
# выводит количество найденных файлов
# 2. снова ожидает ввод
# поиск происходит только среди найденных на этапе 1
# 3. снова ожидает ввод
# ...
# Выход из программы программировать не нужно.
# Достаточно принудительно остановить, для этого можете нажать Ctrl + C

# Пример на настоящих данных

# python3 find_procedure.py
# Введите строку: INSERT
# ... большой список файлов ...
# Всего: 301
# Введите строку: APPLICATION_SETUP
# ... большой список файлов ...
# Всего: 26
# Введите строку: A400M
# ... большой список файлов ...
# Всего: 17
# Введите строку: 0.0
# Migrations/000_PSE_Application_setup.sql
# Migrations/100_1-32_PSE_Application_setup.sql
# Всего: 2
# Введите строку: 2.0
# Migrations/000_PSE_Application_setup.sql
# Всего: 1

# не забываем организовывать собственный код в функции
# на зачёт с отличием, использовать папку 'Advanced Migrations'

import glob
import os.path


def files_list():
    migrations = input('Укажите путь к директории с файлами: ')
    files = glob.glob(os.path.join(migrations, "*.sql"))
    for file in files:
        print('Migrations   ', file)
    return files

def first_user_request():
    file_copy = files_list()
    while True:
        request = input('Введите строку: ')
        files_request = []
        for file in file_copy:
            contents = open(file).read()
            with open(file) as f:
                contents = f.read()
                if request in contents.rstrip():
                    files_request.append(file)
                    print(len(files_request), file)
                    f.close()
        for file_name in files_request:
            print(file_name)
        print("Всего: ", len(files_request))
        file_copy = files_request
        
first_user_request()
