import Admin
import Database
import User
import Manager

if __name__ == "__main__":

    # Создаем новый обьект класса Database и открываем соединение с базой(подключаемся к ней)

    new_connection = Database.Database()

    print('Добро пожаловать в интернет магазин велосипедов!')
    print('Для продолжения работы зарегистрируйтесь или авторизуйтесь')
    print('1) Регистрация')
    print('2) Авторизация')
    number = int(input())
    role = ''
    if number == 1:

        print('Введите логин:')
        login = input()
        print('Введите пароль:')
        password = input()
        print('Укажите тип аккаунта:')
        role = input()
        if role == 'Admin':
            new_Admin = Admin.Admin()
            new_Admin.insertIntoSecurity(login, role, password)
            role = 'Admin'
            number = 2

        if role == 'User':
            new_User = User.User()
            new_User.insertIntoSecurity(login, role, password)
            role = 'User'
            number = 2

        if role == 'Manager':
            new_manager = Manager.Manager()
            new_manager.insertIntoSecurity(login, role, password)
            role = 'Manager'
            number = 2

    if number == 2:
        print('Введите Ваш логин:')
        login = input()
        print('Введите пароль:')
        password = input()
        rez = new_connection.selectFromSecurity(login)
        if rez[0][0] == login and rez[0][2] == password:
            if rez[0][1] == 'User':
                role = 'User'
                new_User = User.User()
            if rez[0][1] == 'Admin':
                role = 'Admin'
                new_Admin = Admin.Admin()
            if rez[0][1] == 'Manager':
                new_manager = Manager.Manager()
                role = 'Manager'
        else:
            print('Ошибка')

    if role == 'User':
        tovary = new_User.selectFromWareHouse()
        dict1 = {}
        print('Вот весь актуальный список товаров')
        for i in range(len(tovary)):
            print(*tovary[i])
        print('Вы можете изменить свои данные - для этого введите 1')
        print("Вы можете составить корзину из предложенных товаров - для этого введите 2")
        print("Чтобы закончить работу - напишите end")
        num = input()
        while num != 'end':

            if num == '2':
                korzina = []
                for i in range(len(tovary)):
                    print(tovary[i][1], tovary[i][3])
                    dict1.update({tovary[i][1]:tovary[i][3]})
                print('Напишите все Ваши покупки')
                print('Достаточно указывать названия велосипедов, которые хотите купить')
                print('В конце покупок напишите end для завершения программы')
                x = 'abc'

                while x != 'end':
                    x = input()
                    if x != 'end':
                        korzina.append(x)


                        summa = 0

                        for i in range(len(korzina)):

                            summa = summa + dict1[korzina[i]]

                print('Итоговая сумма:', summa)
            if num == '1':
                print('Введите Ваш login:')
                login = input()
                print('Введите параметр который меняем:')
                param1 = input()
                print('Введите параметр на который меняем:')
                param2 = input()
                new_User.updateSecurity(param1, param2, login)

            num = input()

    if role == 'Admin':
        stroka = ''
        print('1) Просмотреть список всех сотрудников')
        print('2) Внести изменения в данные')
        print('3) Удалить сотрудника')
        print('4) Добавить сотрудника')
        print('5) Выбрать сотрудников по задданому критерию')
        print('Для завершения введите end')
        while stroka != 'end':
            stroka = input()

            if stroka != 'end':

                if stroka == '1':

                    rez = new_Admin.selectFromWorkers()

                    for i in range(len(rez)):
                        print(*rez[i])
                if stroka == '2':
                    print('Введите ID:')
                    id = int(input())
                    print('Введите параметр который меняем:')
                    param1 = input()
                    print('Введите параметр на который меняем:')
                    param2 = input()
                    new_Admin.updateWorkers(param1, param2, id)


                if stroka == '3':
                    print('Введите ID сотрудника, которого хотите удалить:')
                    id = int(input())
                    new_Admin.deleteFromWorkers(id)


                if stroka == '4':
                    print('Введите через пробел ID, имя, должность нового сотрудника:')
                    stroka = input().split(' ')

                    new_Admin.insertIntoWorkers(int(stroka[0]), stroka[1], stroka[2])



                if stroka == '5':

                    param1 = input('Введите параметр по которому хотите сделать выборку:')

                    param2 = input('Введите значение желаемого параметра:')

                    rez = new_Admin.select1FromWorkers(param1, param2)

                    for i in range(len(rez)):
                        print(*rez[i])
    if role == 'Manager':
        print('1) Просмотреть список всех товаров')
        print('2) Внести изменения в данные')
        print('3) Удалить товар')
        print('4) Добавить товар')
        print('5) Выбрать товары по задданому критерию')
        print('Для завершения введите end')
        stroka = ''
        while stroka != 'end':
            stroka = input()

            if stroka != 'end':
                if stroka == '1':

                    rez = new_manager.selectFromWareHouse()

                    for i in range(len(rez)):
                        print(*rez[i])
                if stroka == '2':
                    print('Введите ID:')
                    id = int(input())
                    print('Введите параметр который меняем:')
                    param1 = input()
                    print('Введите параметр на который меняем:')
                    param2 = input()
                    new_manager.updateWarehouse(param1, param2, id)


                if stroka == '3':
                    print('Введите ID товара, который хотите удалить:')
                    id = int(input())
                    new_manager.deleteFromWarehouse(id)


                if stroka == '4':
                    print('Введите через пробел ID, имя, количество, цену нового товара:')
                    stroka = input().split(' ')

                    new_manager.insertIntoWarehouse(stroka[0], stroka[1], stroka[2], stroka[3])



                if stroka == '5':

                    param1 = input('Введите параметр по которому хотите сделать выборку:')

                    param2 = input('Введите значение желаемого параметра:')

                    rez = new_manager.select1FromWarehouse(param1, param2)

                    for i in range(len(rez)):
                        print(*rez[i])
