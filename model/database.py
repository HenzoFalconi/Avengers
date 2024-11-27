import mysql.connector
from mysql.connector import Error
from os import getenv

class Database:
    def __init__(self):
        self.host = getenv('BD_HOST')
        self.user = getenv('BD_USER')
        self.password = getenv('BD_PSWD')
        self.database = getenv('BD_DATABASE')

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host = self.host,
                user = self.user,
                password = self.password,
                database = self.database
            )
            self.cursor = self.connection.cursor()
            print('Conexão com o banco de dados realizada com sucesso')
        except Error as e:
            print(f'Erro: {e}')

Database().connect()

