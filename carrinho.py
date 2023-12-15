class Carrinho:
    def __init__(self):
        self.carrinho = []
        self.preco_total_carrinho = []


    def deletar_item_carrinho(self, nome_produto):
        for item in self.carrinho:
            if item[0] == nome_produto:
                self.preco_total_carrinho.remove(item[2])
                self.carrinho.remove(item)
                break


