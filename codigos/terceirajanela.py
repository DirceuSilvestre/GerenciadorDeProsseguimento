from tkinter import *

def janela3(nome_categoria):
    janela3 = Tk()
    janela3.title("Gerenciador de Prosseguimento")
    janela3.geometry("500x600")

    # Exibir A Lista #

    lista_exibir = Listbox(janela3, font=('Comic Sans', 20), selectmode=SINGLE)
    arquivo_categorias = open(nome_categoria, "a")
    arquivo_categorias.close()
    arquivo_categorias = open(nome_categoria, "r")
    arquivo_lido = arquivo_categorias.readlines()
    arquivo_categorias.close()
    for item in arquivo_lido:
        lista_exibir.insert(END, item)
    lista_exibir.place(height= 200, x = 100, y = 150)

    # Caixa de Texto #

    nome_obra = Entry(janela3, bd=2, font=("Calibri", 15), justify=CENTER)
    nome_obra.place(width=300, height=40, x=100, y=460)

    # Funções #

    def exibir_atualizacao():
        global lista_exibir
        lista_exibir = Listbox(janela3, font=('Comic Sans', 20), selectmode=SINGLE)
        arquivo_categorias = open(nome_categoria, "a")
        arquivo_categorias.close()
        arquivo_categorias = open(nome_categoria, "r")
        arquivo_lido = arquivo_categorias.readlines()
        arquivo_categorias.close()
        for item in arquivo_lido:
            lista_exibir.insert(END, item)
        lista_exibir.place(height= 200, x = 100, y = 150)

    def incluir_obra():
        nome = str(nome_obra.get())
        lista_exibir.insert(END, nome)
        arquivo_categorias = open(nome_categoria, "a")
        arquivo_categorias.write(nome + ' \n')
        arquivo_categorias.close()
        exibir_atualizacao()

    def excluir_obra():
        nome = str(nome_obra.get())
        arquivo_categorias = open(nome_categoria, "r")
        arquivo_lido = arquivo_categorias.readlines()
        arquivo_categorias.close()
        lista_conteudo = [s for s in arquivo_lido if nome[0:(len(nome)//2)] in s]
        if lista_conteudo != []:
            local = arquivo_lido.index(lista_conteudo[0])
            arquivo_lido.remove(lista_conteudo[0])
            arquivo_categorias = open(nome_categoria, "w")
            arquivo_categorias.writelines(arquivo_lido)
            arquivo_categorias.close()
        exibir_atualizacao()

    def alterar_obra():
        nome = str(nome_obra.get())
        arquivo_categorias = open(nome_categoria, "r")
        arquivo_lido = arquivo_categorias.readlines()
        arquivo_categorias.close()
        lista_conteudo = [s for s in arquivo_lido if nome[0:(len(nome)//2)] in s]
        if lista_conteudo != []:
            local = arquivo_lido.index(lista_conteudo[0])
            arquivo_lido.remove(lista_conteudo[0])
            arquivo_lido.insert(local, str(nome + ' \n'))
            arquivo_categorias = open(nome_categoria, "w")
            arquivo_categorias.writelines(arquivo_lido)
            arquivo_categorias.close()
        exibir_atualizacao()

    def pegar_obra():
        nome = lista_exibir.get(ACTIVE)
        nome_obra.insert(0, nome[0:-2])
        exibir_atualizacao()

    # Labels #

    lab_secundaria = Label(janela3, text=nome_categoria[0:-4], font=('Times New Roman', 25))
    lab_secundaria.pack(side='top')

    # Botões #

    botao_pegar = Button(janela3, text='PEGAR', command=pegar_obra)
    botao_pegar.place(x=230, y=415)

    botao_incluir = Button(janela3, text='INCLUIR', command=incluir_obra)
    botao_incluir.place(x=100, y=520)

    botao_excluir = Button(janela3, text='EXCLUIR', command=excluir_obra)
    botao_excluir.place(x=343, y=520)

    botao_alterar = Button(janela3, text='ALTERAR', command=alterar_obra)
    botao_alterar.place(x=230, y=520)

    janela3.mainloop()