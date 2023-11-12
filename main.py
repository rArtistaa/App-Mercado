class Produto:
    def __init__(self):
        self.produtos = {}

    def adicionar_produto(self, nome, preco, quantidade):
        if self.produtos:
            last_id = max(self.produtos.keys())
            id = last_id + 1
        if not self.produtos:
            self.produtos.update({1: [nome, preco, quantidade]})
        else:
            self.produtos.update({id: [nome, preco, quantidade]})

    def showProducts(self):
        print(self.produtos)

produto = Produto()
produto.adicionar_produto('Arroz', 'R$ 12,00', 43)
