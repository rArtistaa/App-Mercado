import tkinter as tk
from tkinter.font import Font
from tkinter import messagebox
import customtkinter as ctk
from clientes import Cliente
from produtos import Produto


class AcessoMercado(Cliente):
    def __init__(self):
        Cliente.__init__(self)
        Produto.__init__(self)

        self.clientes = Cliente()

        ctk.set_appearance_mode('dark')

        self.main_root = ctk.CTk()
        self.main_root.geometry('650x540+360+60')
        self.main_root.resizable(False, False)
        self.main_root.title('Area de acesso')

        #font1 = Font(font='8514oem', size=20, slant='italic', weight='bold')
        # Frame cinza
        self.frame = ctk.CTkFrame(self.main_root, width=1200, height=1200, corner_radius=12, bg_color='#282424',
                                  fg_color='#bfbdbd')
        self.frame.pack(padx=12, pady=20)

        # Frame branco
        self.frame2 = ctk.CTkFrame(self.frame, width=555, height=380, corner_radius=16, bg_color='#bfbdbd',
                                   fg_color='white')
        self.frame2.place(x=35, y=75)

        #

        self.titulo = tk.Label(self.frame, bg='#bfbdbd', text='Mercado 0800', font='Arial 22 italic bold')
        self.titulo.place(x=210, y=20)

        self.area_do_cliente = tk.Label(self.frame2, bg='white', text='Área do Cliente', font='Arial 16 bold')
        self.area_do_cliente.place(x=200, y=12)

        self.cadastro_label = ctk.CTkLabel(self.frame2, text='Cadastro', font=('Arial bold', 15), text_color='black')
        self.cadastro_label.place(x=110, y=60)


        # Login frame

        self.login_entry = ctk.CTkEntry(self.frame2, width=180, placeholder_text='username', placeholder_text_color='grey',
                                        fg_color='white', corner_radius=0, text_color='black')
        self.login_entry.place(x=50, y=120)

        self.password_entry = ctk.CTkEntry(self.frame2, width=180, placeholder_text='password', placeholder_text_color='grey',
                                           fg_color='white', corner_radius=0, text_color='black')
        self.password_entry.configure(show='*')
        self.password_entry.place(x=50, y=170)

        self.telefone_entry = ctk.CTkEntry(self.frame2, width=180, placeholder_text='telefone', placeholder_text_color='grey',
                                           fg_color='white', corner_radius=0, text_color='black')
        self.telefone_entry.place(x=50, y=240)

        self.ja_sou_cliente = tk.Label(self.frame, bg='white', text='Já sou cliente', font='Arial 10 italic underline',
                                       cursor='hand2')


        self.checkbox_actv = ctk.DoubleVar()
        self.checkbox = ctk.CTkCheckBox(self.frame2, text='show password', corner_radius=6, border_width=2, variable=self.checkbox_actv,
                                        command=self.show_password, checkbox_width=17, checkbox_height=17,
                                        text_color='black')
        self.checkbox.place(x=50, y=205)

        self.linha_sep = ctk.CTkLabel(self.frame2, width=1, height=200,bg_color='black', text='')
        self.linha_sep.place(x=275, y=80)

        self.criar_button = ctk.CTkButton(self.frame2, corner_radius=10, text='Criar', text_color='black',
                                            font=('Arial bold', 16), fg_color='green', hover_color='dark green',
                                            width=100, height=27, command=self.criar_conta)
        self.criar_button.place(x=90, y= 300)

        # Area para Entrar

        self.entrar_label = ctk.CTkLabel(self.frame2, text_color='black', text='Entrar', font=('Arial bold', 15))
        self.entrar_label.place(x=390, y=60)

        self.login_entrar_entry = ctk.CTkEntry(self.frame2, width=180, placeholder_text='username',
                                               placeholder_text_color='grey', fg_color='white', corner_radius=0,
                                               text_color='black')
        self.login_entrar_entry.place(x=320, y=120)

        self.password_entrar_entry = ctk.CTkEntry(self.frame2, width=180, placeholder_text='password',
                                           placeholder_text_color='grey',
                                           fg_color='white', corner_radius=0, text_color='black')
        self.password_entrar_entry.configure(show='*')
        self.password_entrar_entry.place(x=320, y=170)

        self.checkbox_actv2 = ctk.DoubleVar()
        self.checkbox2 = ctk.CTkCheckBox(self.frame2, text='show password', corner_radius=6, border_width=2,
                                        variable=self.checkbox_actv2,
                                        command=self.show_password, checkbox_width=17, checkbox_height=17,
                                        text_color='black')
        self.checkbox2.place(x=320, y=205)

        self.entrar_button = ctk.CTkButton(self.frame2, corner_radius=10, text='Entrar', text_color='black',
                                          font=('Arial bold', 16), fg_color='green', hover_color='dark green',
                                          width=100, height=27, command=self.verificar_conta)
        self.entrar_button.place(x=360, y=300)



    def criar_conta(self):
        login = self.login_entry.get()
        senha = self.password_entry.get()
        telefone = self.telefone_entry.get()

        for cliente in self.clientes.clientes:
            if cliente[1] == login and cliente[3] == telefone:
                messagebox.showwarning('Cadastro inválido', 'Nome de usuário e número de telefone já cadastrados')
                return
            elif cliente[1] == login:
                messagebox.showwarning('Usuário inválido', 'Nome de usuário já cadastrado')
                return
            elif cliente[3] == telefone:
                messagebox.showwarning('Telefone inválido', 'Número de telefone já cadastrado')

        if len(login) < 7:
            messagebox.showwarning('Usuário curto', 'Nome de usuário muito curto')
            return

        if len(telefone) != 11:
            messagebox.showwarning('Telefone inválido', 'Formato do número de telefone inválido\nTente(xx)xxxx xxxx')
            return

        if len(senha) < 8:
            messagebox.showwarning('Senha inválida', 'Digite uma senha com pelo menos 7 caracteres')
            return

        self.clientes.adicionar_cliente(login, senha, telefone)
        messagebox.showinfo('Cadastro concluído', 'Usuário cadastrado com sucesso')
        self.login_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.telefone_entry.delete(0, tk.END)


    def verificar_conta(self):
        login = self.login_entrar_entry.get()
        senha = self.password_entrar_entry.get()

        for cliente in self.clientes.clientes:
            if login == cliente[1] and senha == cliente[2]:
                messagebox.showinfo('Logado', 'Usuário validado, entrando no mercado')
                self.main_root.destroy()
                return

        messagebox.showwarning('Usuário inválido', 'Nome de usuário ou senha incorretos.\nTente novamente')
        self.login_entrar_entry.delete(0, tk.END)
        self.password_entrar_entry.delete(0, tk.END)


    def show_password(self):
        if self.checkbox_actv.get() == 1:
            self.password_entry.configure(show='')
        else:
            self.password_entry.configure(show='*')

        if self.checkbox_actv2.get() == 1:
            self.password_entrar_entry.configure(show='')
        else:
            self.password_entrar_entry.configure(show='*')

