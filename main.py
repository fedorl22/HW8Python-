import sys
import sqlite3 



def print_menu():  
    print ('\n Пожалуйста, выберите один из следующих пунктов:')  
    print('1. Добавить новый контакт')  
    print('2. Показать все контакты')  
    print('3. Редактировать контакт')  
    print('4. Удалить запись')
    print('5. Найти контакт')
    print('0. Выход из телефонной книги')

def addcontact():
    while True:  
        Name = input("Введите имя: ") 
        if len(Name) != 0:  
            break  
        else:  
            print("Пожалуйста, введите корректное имя нового контактного лица")
    while True:  
        Patronymic = input("Введите отчество: ") 
        if len(Patronymic) != 0:  
            break  
        else:  
            print("Пожалуйста, введите корректное отчество нового контактного лица")                 
    while True:  
        Surname = input("Введите фамилию ")  
        if len(Surname) != 0:  
            break  
        else:  
            print("Пожалуйста, введите корректную фамилию нового контактного лица")    
    while True:  
        Phone_number = input("Введите номер телефона? (допускаются только 11 цифр): ")  
        if not Phone_number.isdigit():  
            print("Пожалуйста, введите 11-значный номер телефона без +, запятой, пробелов и знаков препинания")  
            continue  
        elif len(Phone_number) != 11:  
            print("Пожалуйста, введите 11-значный номер телефона без +, запятой, пробелов и знаков препинания")  
            continue  
        else:  
            break  
    cursor.execute('''INSERT INTO phonebook (Name, Patronymic, Surname, Phone_number) VALUES (?,?,?,?)''',
                                                                         (Name, Patronymic, Surname, Phone_number))  
    conn.commit()      
    print("New contact " + Surname + ' ' + Patronymic + ' ' + Name + " was added to the phonebook table")

def displaybook():
    cursor.execute("SELECT Surname, Patronymic, Name, phone_number FROM phonebook ORDER BY surname")
    results = cursor.fetchall()
    print(results)

def key_pair_reception(str):
    print ("\nПожалуйста, выберите поле " + str + " (от 1 до 4)")  
    print('1. Имя') 
    print('2. Отчество') 
    print('3. Фамилия')  
    print('4. Телефон')  
    print('0. Вернуться в главное меню')
    n = int(input('Ваш выбор : '))
    if n == 1:  
        field = "Name"
    elif n == 2:  
        field = "Patronymic"
    elif n == 3:  
        field = "Surname"
    elif n == 4:  
        field = "Phone_number"
    else:
        return None
    keyword = input("\nПожалуйста, введите значение поля: " + field + " = ")
    keypair = field + "='" + keyword + "'"
    return keypair

def editcontacts():
    s = key_pair_reception('записи')
    u = key_pair_reception('обновления')
    if s != None:
        sql = "UPDATE phonebook SET " + u + " WHERE " + s
        cursor.execute(sql)
        conn.commit()
        print("Запись с  " + s + " обновлена.\n")

def deletecontacts():
    s = key_pair_reception('записи')
    if s != None:
        sql = 'DELETE FROM phonebook WHERE ' + s
        cursor.execute(sql)
        conn.commit()
        print("Запись с " + s + " удалена.\n")

def findcontacts():
    s = key_pair_reception('записи')
    if s != None:
        sql = 'SELECT Surname, Patronymic, Name, Phone_number FROM phonebook WHERE ' + s + ' ORDER BY surname'
        cursor.execute(sql)
        results = cursor.fetchall()
        print(results)

# Основная программа
print ('\nДобро пожаловать в телефонную книжку')
conn = sqlite3.connect('PhoneBook.db')  
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS phonebook (
                id integer PRIMARY KEY,
                Name text NOT NULL,
                Patronymic text,
                Surname text,
                Phone_number text)''');
m = -1  
while m != 0:
    print_menu()  
    m = int(input('Выберите режим: '))  
    if m == 1:  
        addcontact()
        continue
    elif m == 2:  
        displaybook()
        continue
    elif m == 3:  
        editcontacts()
        continue
    elif m == 4:  
        deletecontacts()
        continue
    elif m == 5:  
        findcontacts()
        continue
    elif m == 0:  
        print('Телефонная книжка завершает свою работу, спасибо что пользовались нашими услугами.\n')
        conn.close()
        sys.exit(0)  
    else:  
        print('Следуйте инструкциям')