class Carrinho:
    def __init__(self):
        self.carrinho = []
        self.preco_total_carrinho = []


    def deletar_item_carrinho(self, nome_produto):
        for item in self.carrinho:
            if item[0] == nome_produto:
                self.carrinho.remove(item)

    def mostrar_carrinho(self):
        return [item for item in self.carrinho]

