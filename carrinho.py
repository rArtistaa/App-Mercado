class Carrinho:
    def __init__(self):
        self.carrinho = []
        self.preco_total_carrinho = []


    def mostrar_carrinho(self):
        return [item for item in self.carrinho]

