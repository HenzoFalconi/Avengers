import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
from os import getenv

class Database:
    def __init__(self):
        """Inicializa a classe e carrega variáveis de ambiente."""
        load_dotenv()
        self.host = getenv('BD_HOST')
        self.user = getenv('BD_USER')
        self.password = getenv('BD_PSWD')
        self.database = getenv('BD_DATABASE')
        self.connection = None
        self.cursor = None

    def connect(self):
        """Estabelece conexão com o banco de dados."""
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor()
            print('Conexão com o banco de dados realizada com sucesso!')
        except Error as e:
            print(f'Erro ao conectar ao banco de dados: {e}')

    def disconnect(self):
        """Encerra a conexão com o banco de dados."""
        if self.connection:
            self.cursor.close()
            self.connection.close()
            print('Conexão com o banco de dados encerrada com sucesso!')

    def execute_query(self, query, values=None):
        """Executa uma query genérica."""
        try:
            self.cursor.execute(query, values)
            self.connection.commit()
            print('Query executada com sucesso!')
            return self.cursor
        except Error as e:
            print(f'Erro ao executar query: {e}')
            return None

    def select(self, query, values=None):
        """Executa uma query de seleção."""
        try:
            self.cursor.execute(query, values)
            return self.cursor.fetchall()
        except Error as e:
            print(f'Erro ao executar SELECT: {e}')
            return None

    def verificar_tornozeleira_existe(self, id_tornozeleira):
        """Verifica se uma tornozeleira existe no banco de dados."""
        try:
            query = "SELECT 1 FROM tornozeleira WHERE idtornozeleira = %s"
            self.cursor.execute(query, (id_tornozeleira,))
            return self.cursor.fetchone() is not None
        except Error as e:
            print(f"Erro ao verificar tornozeleira: {e}")
            return False

    def atualizar_tornozeleira(self, id_tornozeleira, status):
        """Atualiza o status da tornozeleira."""
        try:
            if not self.verificar_tornozeleira_existe(id_tornozeleira):
                print(f"Tornozeleira com ID {id_tornozeleira} não encontrada.")
                return

            query = """
            UPDATE tornozeleira
            SET status = %s, data_ativacao = NOW()
            WHERE idtornozeleira = %s
            """
            self.cursor.execute(query, (status, id_tornozeleira))
            self.connection.commit()
            print("Tornozeleira atualizada com sucesso!")
        except Error as e:
            print(f"Erro ao atualizar tornozeleira: {e}")

    def verificar_status_tornozeleira(self, id_tornozeleira):
        """Verifica o status atual de uma tornozeleira."""
        try:
            query = "SELECT status, data_ativacao, data_desativacao FROM tornozeleira WHERE idtornozeleira = %s"
            self.cursor.execute(query, (id_tornozeleira,))
            result = self.cursor.fetchone()
            if result:
                print(f"Status da tornozeleira {id_tornozeleira}: {result}")
            else:
                print(f"Nenhuma tornozeleira encontrada com ID {id_tornozeleira}.")
        except Error as e:
            print(f"Erro ao verificar status da tornozeleira: {e}")

    def inserir_convocacao(self, motivo, data_convocacao, status, id_heroi):
        """Insere uma nova convocação no banco de dados."""
        try:
            query = """
            INSERT INTO convocacao (motivo, data_convocacao, status, idheroi)
            VALUES (%s, %s, %s, %s)
            """
            self.cursor.execute(query, (motivo, data_convocacao, status, id_heroi))
            self.connection.commit()
            print("Convocação inserida com sucesso!")
        except Error as e:
            print(f"Erro ao inserir convocação: {e}")


if __name__ == "__main__":
    # Instancia e utiliza a classe Database
    db = Database()
    db.connect()

    # Atualizar o status da tornozeleira
    db.atualizar_tornozeleira(1, "ativa")
    
    # Verificar o status da tornozeleira
    db.verificar_status_tornozeleira(1)

    # Inserir uma nova convocação
    db.inserir_convocacao(
        "Reunião urgente",
        "2024-12-05 10:00:00",
        "pendente",
        1
    )

    # Desconectar do banco de dados
    db.disconnect()
