from tkinter import *

def janela3(nome_categoria):
    janela3 = Tk()
    janela3.title("Gerenciador de Prosseguimento")
    janela3.geometry("500x600")

    # Exibir A Lista #

    lista_exibir = Listbox(janela3, font=('Comic Sans', 20))
    arquivo_categorias = open(nome_categoria, "a")
    arquivo_categorias.close()
    arquivo_categorias = open(nome_categoria, "r")
    arquivo_lido = arquivo_categorias.readlines()
    arquivo_categorias.close()
    for item in arquivo_lido:
        lista_exibir.insert(END, item)
    lista_exibir.place(height= 200, x = 100, y = 150)

    # Funções #

    def exibir_atualizacao():
        global lista_exibir
        arquivo_categorias = open(nome_categoria, "a")
        arquivo_categorias.close()
        arquivo_categorias = open(nome_categoria, "r")
        arquivo_lido = arquivo_categorias.readlines()
        arquivo_categorias.close()
        for item in arquivo_lido:
            lista_exibir.insert(END, item)
        lista_exibir.place(height= 200, x = 100, y = 150)

    def incluir_obra():
        nome = str(nome_categoria.get())
        lista_exibir.insert(END, nome)
        arquivo_categorias = open(nome_categoria, "a")
        arquivo_categorias.write(nome + ' \n')
        arquivo_categorias.close()
        exibir_atualizacao()

    def excluir_obra():
        pass

    def alterar_obra():
        pass

    # Labels #

    lab_secundaria = Label(janela3, text=nome_categoria[0:-4], font=('Times New Roman', 25))
    lab_secundaria.pack(side='top')

    # Botões #

    botao_incluir = Button(janela3, text='INCLUIR', command=incluir_obra)
    botao_incluir.place(x=100, y=520)

    botao_excluir = Button(janela3, text='EXCLUIR', command=excluir_obra)
    botao_excluir.place(x=343, y=520)

    botao_alterar = Button(janela3, text='ALTERAR', command=alterar_obra)
    botao_alterar.place(x=230, y=520)

    janela3.mainloop()