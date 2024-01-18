import mysql.connector

# Сюда вписать данные от своего пользователя и пароль

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Zerg",
        database="Shop",
    )
    print(connection)
    cursor = connection.cursor()
except mysql.connector.Error as e:
    print(e)
class Database:

    def insertIntoClients(self, id, name, personalSale, Role):
        try:
            if type(id) != int or type(name) != str or type(personalSale) != str:
                raise TypeError
            query = f"INSERT INTO Clients (id, name, personalSale) VALUES (%s, %s, %s);"
            cursor.execute(query, (id, name, personalSale))
            connection.commit()
        except mysql.connector.Error as e:
            print(e)



    def insertIntoHistory(self, id, listOfProducts, date, Role):
        try:
            if type(id) != int or type(listOfProducts) != str or type(date) != str:
                raise TypeError
            query = f"INSERT INTO History (id, listOfProducts, date) VALUES (%s, %s, %s);"
            cursor.execute(query, (id, listOfProducts, date))
            connection.commit()
        except mysql.connector.Error as e:
            print(e)

    def insertIntoWarehouse(self, id, nameProduct, sale, countOfProduct = 0, Role = ''):
        flag = 0
        try:
            if type(id) != int or type(nameProduct) != str or type(countOfProduct) != str:
                raise TypeError
        except TypeError:
            print('Ошибка типов')
            flag = 1
        if flag == 0:
            try:

                query = f"INSERT INTO Warehouse (id, nameProduct, countOfProduct, sale) VALUES (%s, %s, %s, %s);"
                cursor.execute(query, (id, nameProduct, countOfProduct, sale))
                connection.commit()
            except mysql.connector.Error as e:
                print(e)

    def insertIntoWorkers(self, id, name, role, Role = ''):
        flag = 0
        try:
            if type(id) != int or type(name) != str or type(role) != str:
                raise TypeError
        except TypeError:
            print('Ошибка типов!')
            flag = 1
        if flag == 0:
            try:
                query = f"INSERT INTO Workers (id, name, role) VALUES (%s, %s, %s);"
                cursor.execute(query, (id, name, role))
                connection.commit()
                return 0
            except mysql.connector.Error as e:
                print(e)

    def insertIntoSecurity(self, login = '', role = '', password = ''):

        try:
            if type(login) != str or type(role) != str or type(password) != str:
                raise TypeError
            query = f"INSERT INTO Security (login, role, password) VALUES (%s, %s, %s);"
            cursor.execute(query, (login, role, password))
            connection.commit()
        except mysql.connector.Error as e:
            print(e)

    def updateClients(self, paramOnUpdate, newParam, id = 0, Role = ''):

        try:
            if type(paramOnUpdate) != str or type(newParam) != str or type(id) != int:
                raise TypeError
            update_query = f"""
                        UPDATE
                            Clients
                        SET
                            %s = '%s'
                        WHERE
                            id = %s;
                            """ % (paramOnUpdate, newParam, id)

            cursor.execute(update_query)
            connection.commit()
        except mysql.connector.Error as e:
            print(e)

    def updateSecurity(self, paramOnUpdate, newParam, login, Role = ''):
        flag = 0
        try:
            if type(paramOnUpdate) != str or type(newParam) != str or type(login) != str:
                raise TypeError
        except TypeError:
            print('Ошибка типов!')
            flag = 1
        try:
            if flag == 0:
                update_query = f"UPDATE Security SET {paramOnUpdate} = '{newParam}' WHERE login = '{login}';"
                cursor.execute(update_query)
                connection.commit()
        except mysql.connector.Error as e:
            print(e)

    def updateWorkers(self, paramOnUpdate, newParam, id = 0, Role = ''):
        flag = 0
        try:
            if type(paramOnUpdate) != str or type(newParam) != str or type(id) != int:
                raise TypeError
        except TypeError:
            print('Ошибка типов!')
            flag = 1
        try:
            if flag == 0:
                update_query = f"""
                                        UPDATE
                                            Workers
                                        SET
                                            %s = '%s'
                                        WHERE
                                            id = %s;
                                            """ % (paramOnUpdate, newParam, id)

                cursor.execute(update_query)
                connection.commit()
        except mysql.connector.Error as e:
            print(e)

    def updateWarehouse(self, paramOnUpdate, newParam, id = 0, Role = ''):
        flag = 0
        try:
            if type(paramOnUpdate) != str or type(newParam) != str or type(id) != int:
                raise TypeError
        except TypeError:
            print('Ошибка типов!')
            flag = 1
        if flag == 0:
            try:

                update_query = f"""
                                        UPDATE
                                            Warehouse
                                        SET
                                            %s = '%s'
                                        WHERE
                                            id = %s;
                                            """ % (paramOnUpdate, newParam, id)

                cursor.execute(update_query)
                connection.commit()
            except mysql.connector.Error as e:
                print(e)

    def updateHistory(self, paramOnUpdate, newParam, id = 0, Role = ''):

        try:
            if type(paramOnUpdate) != str or type(newParam) != str or type(id) != int:
                raise TypeError
            update_query = f"""
                                    UPDATE
                                        History
                                    SET
                                        %s = '%s'
                                    WHERE
                                        id = %s;
                                        """ % (paramOnUpdate, newParam, id)

            cursor.execute(update_query)
            connection.commit()
        except mysql.connector.Error as e:
            print(e)

    def selectFromWareHouse(self):
        try:
            query = f"SELECT * FROM Warehouse;"
            cursor.execute(query)
            rez = cursor.fetchall()
            connection.commit()
            return rez
        except mysql.connector.Error as e:
            print(e)

    def selectFromSecurity(self, login = ''):
        flag = 0
        try:
            if type(login) != str:
                raise TypeError
        except TypeError:
            print('Ошибка типов!')
        try:
            query = f"SELECT * FROM Security WHERE login = %s"
            cursor.execute(query, params=(login,))
            rez = cursor.fetchall()
            connection.commit()
            return rez
        except mysql.connector.Error as e:
            print(e)

    def selectFromWorkers(self,):
        try:
            query = f"SELECT * FROM Workers;"
            cursor.execute(query)
            rez = cursor.fetchall()
            connection.commit()
            return rez
        except mysql.connector.Error as e:
            print(e)

    def deleteFromWorkers(self, paramZnach):
        flag = 0
        try:
            if type(paramZnach) != str:
                raise TypeError
        except TypeError:
            print('Ошибка')
            flag = 1
        try:
            if flag == 0:
                query = f"DELETE FROM Workers WHERE id = %s;"
                cursor.execute(query, params=(paramZnach,))
                connection.commit()
        except mysql.connector.Error as e:
            print(e)

    def select1FromWorkers(self, param1, param2):
        flag = 0
        try:
            if type(param1) != str and type(param2) != str:
                raise TypeError
        except TypeError:
            print('Ошибка типов')
            flag = 1
        if flag == 0:
            try:
                query = f"SELECT * FROM Workers WHERE {param1} = '{param2}';"

                cursor.execute(query)
                rez = cursor.fetchall()
                connection.commit()
                return rez
            except mysql.connector.Error as e:
                print(e)

    def select1FromWarehouse(self, param1, param2):

        try:
            if type(param1) != str and type(param2) != str:
                raise TypeError
            query = f"SELECT * FROM Warehouse WHERE {param1} = '{param2}';"

            cursor.execute(query)
            rez = cursor.fetchall()
            connection.commit()
            return rez
        except mysql.connector.Error as e:
            print(e)

    def deleteFromWarehouse(self, paramZnach):
        flag = 0
        try:
            if type(paramZnach) != str:
                raise TypeError
        except TypeError:
            print('Ошибка типов!')
            flag = 1
        if flag == 0:
            try:
                query = f"DELETE FROM Warehouse WHERE id = %s;"
                cursor.execute(query, params=(paramZnach,))
                connection.commit()
            except mysql.connector.Error as e:
                print(e)