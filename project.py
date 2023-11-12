import tkinter as tk
from tkinter.font import Font
from main import *
import random
import customtkinter as ctk


class Mercado(Produto):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode('System')

        self.root = ctk.CTk()
        self.root.geometry('650x540+360+60')
        self.root.resizable(False, False)
        self.root.title('Mercado')


        #self.font1 = Font(font='@KaiTi', size=32, weight='bold')

        self.titulo_principal = tk.Label(self.root, text='Mercadinho', font='Arial 22 bold', height=3, width=30,
                                         bg='light grey')
        self.titulo_principal.place(x=65, y=0)


        self.barra_pesquisas = tk.Entry(self.root, width=25)
        self.barra_pesquisas.place(x=250, y=110)


        self.ver_produtos = tk.Button(self.root, height=2, text='Produtos', relief='raised', overrelief='ridge',)
        self.ver_produtos.place(x=300, y=150)


    def run(self):
        self.root.mainloop()

mercado = Mercado()
mercado.run()
