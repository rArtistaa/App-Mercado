import sqlite3

bd_produtos = sqlite3.connect('produtos_bd')
bd_clientes = sqlite3.connect('clientes_bd')

cursor_produtos = bd_produtos.cursor()
cursor_clientes = bd_clientes.cursor()

#cursor_clientes.execute('CREATE TABLE clientes(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, senha TEXT NOT NULL, telefone TEXT)')

sql_produtos = 'INSERT INTO produtos(nome, categoria, preco, quantidade) VALUES (?, ?, ?, ?)'
sql_clientes = 'INSERT INTO clientes(nome, senha, telefone) VALUES (?, ?, ?)'

#cursor_clientes.execute('DELETE FROM clientes WHERE id = 5')
bd_clientes.commit()


cursor_clientes.close()
bd_clientes.close()