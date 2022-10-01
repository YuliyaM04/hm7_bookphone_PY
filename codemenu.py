from re import search
from secrets import choice
import csv

print('Добро подаловать в справочник')

def main_menu ():
    print('\nМеню')
    print('1. Показать все контакты') #Таблицей
    print('2. Показать все контакты') #сточный
    print('3. Добавить контакты')
    print('4. Экспорт в TXT формате')
    print('5. Экспорт в CSV формате')
    print('6. Импорт из CSV формата')
    print('7. Выход')

    choice = input('Введите пункт: ')
    if choice == '1':
        with open('book.csv',encoding = 'utf-8') as csvfile:
            spamreader = csv.reader(csvfile ,delimiter=';')
            for row in spamreader:
                print(' | '.join(row))
        main_menu()
    elif choice == '2':
        so_data = []
        with open('book.csv',encoding = 'utf-8') as csvfile:
            spamreader = csv.reader(csvfile ,delimiter=';')
            for row in spamreader:
                try:
                    print("Фамилия:"+row[0])
                    print("Имя:"+row[1])
                    print("Телефон:"+row[2])
                    print("Описание1:"+row[3])
                except:
                    print("_______________________________")      
        main_menu()
    elif choice == '3':
        newcontact()
        main_menu()
    elif choice == '4': #export
        so_data = []
        with open('book.csv',encoding = 'utf-8') as csvfile:
            spamreader = csv.reader(csvfile ,delimiter=';')
            for info in spamreader:
                try:
                    file = 'book.txt'
                    with open (file, 'a', encoding = 'utf-8') as data:
                            data.write(f'Фамилия: {info[0]}\nИмя: {info[1]}\nНомер телефона: {info[2]}\nОписание: {info[3]}\n\n')
                except:
                    print("\n")
        print("Ищите файлик book.txt")      
        main_menu()
    elif choice == '5':
        print("Ищите book.csv ")
        main_menu()
    elif choice == '6':
        file=input("Укажите файл для импорта:")
        with open(file,encoding = 'utf-8') as csvfile:
            spamreader = csv.reader(csvfile ,delimiter=';') #, quotechar='|')
            for row in spamreader:
                zapiska = []
                with open (r'book.csv',"a", encoding = 'utf-8' ) as writerowtobook:
                    writer=csv.writer(writerowtobook,delimiter=';', quoting=csv.QUOTE_MINIMAL)
                    writer.writerow(row)
        main_menu()
    elif choice == '7':
        print('Спасибо, что воспользовались справочником!')
    else:
        print('Пожалуйста, введите правильный пункт!')

def newcontact ():
    firstname = input('Введите свое имя: ')
    lastname = input('Введите свою фамилию: ')
    valid =False
    while not valid:
        try:
            phoneNum = input('Введите номер телефона: ')
            if len(phoneNum) != 11:
                print('В номере телефона должно быть 11 цифр.')
            else:
                phoneNum = int(phoneNum)
                valid = True
        except:
            print('Номер телефона должен состоять только из цифр.')
    description = input('Введите описание: ')
    zapis = [lastname,firstname,phoneNum,description]
    with open (r'book.csv',"a", encoding = 'utf-8') as writerowtobook:
        writer=csv.writer(writerowtobook,delimiter=';', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(zapis)
    print('\n_____________________________________________\nКонтакт абонента:' + firstname + ' сохранен успешно.')

main_menu()