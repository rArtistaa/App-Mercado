import tkinter
from tkinter import messagebox
from produtos import Produto
from carrinho import Carrinho
import tkinter as tk
import customtkinter as ctk
import re


class Mercado(Produto, Carrinho):
    def __init__(self):
        # Adicionando outras classes na principal

        Produto.__init__(self)
        Carrinho.__init__(self)

        self.produto = Produto()

        # Mercado
        self.main_root = ctk.CTk()
        self.main_root.geometry('650x540+360+60')
        self.main_root.resizable(False, False)
        self.main_root.title('Mercado')

        # --

        self.titulo_label = tk.Label(self.main_root, text='MERCADO', bg='#282424', fg='white', font='Arial 30 bold')
        self.titulo_label.pack(pady=30)

        # --

        self.produtos_label = tk.Label(self.main_root, text='Produtos', bg='#282424', fg='white',
                                       font='Arial 14 italic bold', cursor='hand2')
        self.produtos_label.place(x=280, y=210)
        self.produtos_label.bind('<Button-1>', self.listar_produtos)

        self.carrinho_label = tk.Label(self.main_root, text='Carrinho', bg='#282424', fg='white',
                                       font='Arial 14 italic bold', cursor='hand2')
        self.carrinho_label.place(x=280, y=270)
        self.carrinho_label.bind('<Button-1>', self.listar_carrinho)


    def listar_produtos(self, event):
        self.root = ctk.CTkToplevel(self.main_root)
        self.root.geometry('480x400+440+170')
        self.root.resizable(False, False)
        self.root.title('Produtos')
        self.root.transient(self.main_root)
        self.root.grab_set()



        produtos_listados_label = tk.Label(self.root, text='Produtos listados', bg='#282424',font='Arial 16', fg='white')
        produtos_listados_label.place(x=150, y=10)


        self.produtos_geral_label = tk.Label(self.root, text='Geral', bg='#282424',font='Arial 10 bold', fg='white', cursor='hand2')
        self.produtos_geral_label.place(x=90, y=70)
        self.produtos_geral_label.bind('<Button-1>', self.mostrar_produto_geral)


        self.produtos_alimentos_label = tk.Label(self.root, text='Alimentos', bg='#282424',font='Arial 10 bold', fg='white', cursor='hand2')
        self.produtos_alimentos_label.place(x=200, y=70)
        self.produtos_alimentos_label.bind('<Button-1>', self.mostrar_produto_alimentos)


        self.produtos_nao_alimentos_label = tk.Label(self.root, text='Não Alimentos', bg='#282424',font='Arial 10 bold', fg='white', cursor='hand2')
        self.produtos_nao_alimentos_label.place(x=320, y=70)
        self.produtos_nao_alimentos_label.bind('<Button-1>', self.mostrar_produto_nao_alimentos)



        self.lista_produtos = tk.Listbox(self.root, width=30, height=12, bg='#d2bdbd', fg='black')
        self.lista_produtos.place(x=145, y=150)
        self.lista_produtos.bind('<<ListboxSelect>>', self.informacao_produto)

    def informacao_produto(self, event):
        self.produto_selecionado = self.lista_produtos.get(self.lista_produtos.curselection())
        self.quantidade = self.pegar_quantidade_produto(self.produto_selecionado)
        self.preco = self.pegar_preco_produto(self.produto_selecionado)

        try:
            self.root2 = ctk.CTkToplevel(self.root)
            self.root2.geometry('400x160+480+300')
            self.root2.title(self.produto_selecionado)
            self.root2.resizable(False, False)
            self.root2.transient(self.root)
            self.root2.grab_set()

            informacao_label = tk.Label(self.root2, text=self.informacao_produto_selecionado(self.produto_selecionado), font='Arial 13 bold', bg='#282424',
                                        fg='white')
            informacao_label.place(x=10, y=10)


            self.quantidade_produto = tk.Scale(self.root2, from_=1, to=self.quantidade, orient='horizontal', relief='solid',
                                          fg='white', bd=0, troughcolor='grey', highlightbackground='#282424',
                                          bg='#282424', activebackground='black', font='Arial 10')
            self.quantidade_produto.place(x=150, y=75)

            botao_confirmar = tk.Button(self.root2, text='Pegar', width=8, height=1, relief='raised', overrelief='ridge', command=self.confirmacao_produto_carrinho)
            botao_confirmar.place(x=170, y=120)


        except tkinter.TclError:
            messagebox.showerror('Erro', 'Selecione uma categoria.')

    def confirmacao_produto_carrinho(self):
        var = self.quantidade_produto.get()
        pergunta = messagebox.askquestion('Confirmar Itens', f'Adicionar {var} unidade(s) de {self.produto_selecionado}\npor R${(self.preco*var):.2f}?')
        if pergunta == 'yes':
            self.carrinho.append([self.produto_selecionado, var, self.preco*var])
            self.preco_total_carrinho.append(self.preco*var)
            messagebox.showinfo('Confirmando', 'Produtos Adicionados ao carrinho com sucesso.')
            self.root2.destroy()
        else:
            messagebox.showinfo('Retornando', 'Voltando sem adicionar os itens ao carrinho.')
            self.root2.destroy()


    def mostrar_produto_geral(self, event):
        lista = self.produtos_gerais()
        self.lista_produtos.delete(0, tk.END)
        for item in lista:
            self.lista_produtos.insert(tk.END, item)

    def mostrar_produto_alimentos(self, event):
        lista = self.produtos_alimentos()
        self.lista_produtos.delete(0, tk.END)
        for item in lista:
            self.lista_produtos.insert(tk.END, item)

    def mostrar_produto_nao_alimentos(self, event):
        lista = self.produtos_nao_alimentos()
        self.lista_produtos.delete(0, tk.END)
        for item in lista:
            self.lista_produtos.insert(tk.END, item)


    def listar_carrinho(self, event):
        self.root_carrinho = ctk.CTkToplevel(self.main_root)
        self.root_carrinho.geometry('480x400+440+170')
        self.root_carrinho.resizable(False, False)
        self.root_carrinho.title('Carrinho')
        self.root_carrinho.transient(self.main_root)
        self.root_carrinho.grab_set()


        self.carrinho_label2 = tk.Label(self.root_carrinho, text='Seu Carrinho', bg='#282424', fg='white', font='Arial 16')
        self.carrinho_label2.place(x=175, y=20)

        self.itens_carrinho = tk.Listbox(self.root_carrinho, width=36, height=12, bg='#d2bdbd', fg='black')
        self.itens_carrinho.place(x=130, y=80)
        self.itens_carrinho.bind('<<ListboxSelect>>', self.informacao_produto_carrinho)
        for item in self.carrinho:
            self.itens_carrinho.insert(tk.END, f'{item[0]:16}Qnt:{item[1]}    R${item[2]:.2f}')


        self.preco_total_label = tk.Label(self.root_carrinho, bg='#282424', fg='white', font='Arial 16 bold', text=f'TOTAL: R${sum(self.preco_total_carrinho):.2f}')
        self.preco_total_label.place(x=160, y=340)

        self.pagar_botao = tk.Button(self.root_carrinho, text='Pagar', width=8, height=1, relief='raised', overrelief='ridge',
                                     command=self.listar_pagamento)
        self.pagar_botao.place(x=380, y=340)

        self.limpar_carrinho_botao = tk.Button(self.root_carrinho, text='Limpar', width=8, height=1, relief='raised', overrelief='ridge',
                                               command=self.limpar_totalmente_carrinho)
        self.limpar_carrinho_botao.place(x=205, y=282)


    def informacao_produto_carrinho(self, event):
        self.produto_selecionado_carrinho = self.itens_carrinho.get(self.itens_carrinho.curselection())

        padrao = re.compile(r'Qnt:(\d+)\s+R\$(\d+\.\d{2})')
        corr = padrao.search(self.produto_selecionado_carrinho)

        quantidade = corr.group(1)
        preco = corr.group(2)

        posicao_substring = self.produto_selecionado_carrinho.find(f'Qnt:{quantidade}    R${preco}')

        nome_produto = self.produto_selecionado_carrinho[:posicao_substring]
        nome_produto = nome_produto.strip()

        excluir_item = messagebox.askquestion('Excluir item', 'Deseja excluir esse item do carrinho?')
        if excluir_item == 'yes':
            self.deletar_item_carrinho(nome_produto)
            self.atualizar_lista_carrinho()
            return

    def atualizar_lista_carrinho(self):
        self.itens_carrinho.delete(0, tk.END)
        for item in self.carrinho:
            self.itens_carrinho.insert(tk.END, f'{item[0]:16}Qnt:{item[1]}    R${item[2]:.2f}')
        self.preco_total_label.configure(text=f'TOTAL: R${sum(self.preco_total_carrinho):.2f}')


    def limpar_totalmente_carrinho(self):
        pergunta = messagebox.askquestion('Limpar carrinho', 'Deseja tirar todos os itens do seu carrinho?')
        if pergunta == 'yes':
            self.carrinho.clear()
            self.preco_total_carrinho.clear()
            self.atualizar_lista_carrinho()
            return

    def pagamento_debito(self):
        self.forma_pagamento_label.config(text='Senha:')
        self.senha_pagamento_entry = tk.Entry(self.root_pagamento, width=12, show='*')
        self.senha_pagamento_entry.place(x=85, y=22)
        self.pagamento_debito_botao.place(x=200, y=200)
        self.pagamento_credito_botao.place(x=200, y=200)

        self.botao_confirmar = tk.Button(self.root_pagamento, width=6, height=1, text='Ok',
                                         relief='raised', overrelief='ridge', command=self.encerrar_programa)
        self.botao_confirmar.place(x=70, y=50)

    def listar_pagamento(self):
        if sum(self.preco_total_carrinho) != 0:
            self.root_pagamento = ctk.CTkToplevel(self.root_carrinho)
            self.root_pagamento.geometry('200x260+750+230')
            self.root_pagamento.resizable(False, False)
            self.root_pagamento.title('Pagamento')
            self.root_pagamento.transient(self.main_root)
            self.root_pagamento.grab_set()

            self.forma_pagamento_label = tk.Label(self.root_pagamento, text='Forma de Pagamento', bg='#282424', fg='white',
                                                  font='Arial 12 bold')
            self.forma_pagamento_label.place(x=18, y=18)

            self.pagamento_debito_botao = tk.Button(self.root_pagamento, text='Débito', width=10, height=1, relief='raised',
                                              overrelief='ridge',command=self.pagamento_debito)
            self.pagamento_debito_botao.place(x=60, y=70)

            self.pagamento_credito_botao = tk.Button(self.root_pagamento, text='Crédito', width=10, height=1, relief='raised',
                                               overrelief='ridge', command=lambda : messagebox.showwarning('Manutenção', 'Método de pagamento temporariamente indisponível\nPor Favor escolha outro.'))
            self.pagamento_credito_botao.place(x=60, y=120)
        else:
            messagebox.showinfo('Carrinho vazio', 'Adicione ao menos 1 item ao carrinho')

    def encerrar_programa(self):
        messagebox.showinfo('Aprovado', 'Pagamento Aprovado!\nObrigado pela preferência.\nVolte sempre.')
        for item in self.carrinho:
            self.subtrair_quantidade_produto(item[0], item[1])
        self.root_pagamento.destroy()
        self.root_carrinho.destroy()
        self.main_root.destroy()
