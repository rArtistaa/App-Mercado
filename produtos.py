import sqlite3


class Produto:
    def __init__(self):
        self.conn = sqlite3.connect('produtos_bd')
        self.cursor = self.conn.cursor()
        query_geral = 'SELECT nome FROM produtos'
        self.__produtos_geral = self.cursor.execute(query_geral).fetchall()


    def produtos_gerais(self):
        query = 'SELECT nome FROM produtos ORDER BY nome ASC'
        self.cursor.execute(query)
        resultados = self.cursor.fetchall()

        return [resultado[0] for resultado in resultados]

    def produtos_alimentos(self):
        query = 'SELECT nome FROM produtos WHERE categoria IN (?, ?, ?, ?, ?, ?, ?, ?, ?) ORDER BY nome ASC'
        self.cursor.execute(query, ('Alimentos', 'Bebidas', 'Carnes', 'Congelados', 'Enlatados', 'Frutas', 'Lanches', 'Laticínios', 'Pães'))
        resultados = self.cursor.fetchall()

        return [resultado[0] for resultado in resultados]


    def pegar_quantidade_produto(self, produto):
        query = 'SELECT quantidade FROM produtos WHERE nome = ?'
        self.cursor.execute(query, (produto,))
        quantidade = self.cursor.fetchone()

        return quantidade


    def pegar_preco_produto(self, produto):
        query = 'SELECT preco FROM produtos WHERE nome = ?'
        self.cursor.execute(query, (produto,))
        preco = self.cursor.fetchone()

        return preco[0]


    def produtos_nao_alimentos(self):
        query = 'SELECT nome FROM produtos WHERE categoria IN (?, ?) ORDER BY nome ASC'
        self.cursor.execute(query, ('Higiene', 'Limpeza'))
        resultados = self.cursor.fetchall()

        return [resultado[0] for resultado in resultados]

    def informacao_produto_selecionado(self, produto):
        query = 'SELECT nome, preco, quantidade FROM produtos WHERE nome = ?'
        self.cursor.execute(query, (produto,))
        resultado = self.cursor.fetchone()

        nome = produto
        preco = float(resultado[1])
        quantidade = int(resultado[2])

        return (f'{"Produto":^20} | {"Preço":^13} | {"Quantidade":^19}\n\n'
                f'{nome:<22}R${preco:<12}{quantidade}')


    def subtrair_quantidade_produto(self, produto, quantidade_comprada):
        quantidade_atual = self.pegar_quantidade_produto(produto)
        nova_quantidade = quantidade_atual[0] - quantidade_comprada

        self.cursor.execute('UPDATE produtos SET quantidade = ? WHERE nome = ?', (nova_quantidade, produto))
        self.conn.commit()
