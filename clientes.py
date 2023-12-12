import sqlite3


class Cliente:
    def __init__(self):
        self.conn = sqlite3.connect('clientes_bd')
        sql = 'SELECT * FROM clientes'
        self.cursor = self.conn.cursor()
        self.sql_clientes = 'INSERT INTO clientes(nome, senha, telefone) VALUES (?, ?, ?)'
        self.clientes = self.cursor.execute(sql).fetchall()


    def adicionar_cliente(self, nome, senha, telefone):
        self.cursor.execute(self.sql_clientes, [nome, senha, telefone])
        self.conn.commit()
