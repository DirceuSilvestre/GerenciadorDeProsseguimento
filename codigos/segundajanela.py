from re import T
from tkinter import *

def janela2():
    janela2 = Tk()
    janela2.title("Gerenciador de Prosseguimento")
    janela2.geometry("500x600")

    # Labels #
    lab_secundaria = Label(janela2, text="Categoria", font=('Times New Roman', 40))
    lab_secundaria.pack(side='top')

    #---------------- Função ------------------#
    #
    #   conectar no sql, verificar se há tabelas
    #   se houver tabelas retornar a quantidade
    #   se não houver retorna 0
    #   faz um for que cria um botão para cada nome de tabela
    #   cada botão chama a terceira janela
    #   e passa o nome da categoria como argumento
    #
    

    # Botões #

    #botão incluir
    botao_incluir = Button(janela2, width = 15, text='Incluir')
    botao_incluir.place(x=100, y=520)

    #botão excluir
    botao_excluir = Button(janela2, width=15, text='Excluir')
    botao_excluir.place(x=285, y=520)

    # Escrita #
    entrada_categoria = StringVar()
    
    nome_categoria = Entry(janela2, bd=2, font=("Calibri", 15), justify=CENTER, textvariable=entrada_categoria)
    
    nome_categoria.place(width=300, height=40, x=100, y=460)

    janela2.mainloop()
