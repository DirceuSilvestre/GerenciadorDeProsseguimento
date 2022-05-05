from asyncio.windows_events import NULL
from tkinter import *
from terceirajanela import janela3

def janela2():

    # Criar A Janela #

    janela2 = Tk()
    janela2.title("Gerenciador de Prosseguimento")
    janela2.geometry("500x600")

    # Mostrar Nome No Topo #

    lab_secundaria = Label(janela2, text="Categoria", font=('Times New Roman', 40))
    lab_secundaria.pack(side='top')

    # Exibir A Lista #

    lista_exibir = Listbox(janela2, font=('Comic Sans', 20))
    arquivo_categorias = open("categorias.txt", "a")
    arquivo_categorias.close()
    arquivo_categorias = open("categorias.txt", "r")
    arquivo_lido = arquivo_categorias.readlines()
    arquivo_categorias.close()
    for item in arquivo_lido:
        lista_exibir.insert(END, item)
    lista_exibir.place(height= 200, x = 100, y = 150)

    # Caixa de Texto #

    nome_categoria = Entry(janela2, bd=2, font=("Calibri", 15), justify=CENTER)
    nome_categoria.place(width=300, height=40, x=100, y=460)

    # Funções #

    def exibir_atualizacao():
        global lista_exibir
        lista_exibir = Listbox(janela2, font=('Comic Sans', 20))
        arquivo_categorias = open("categorias.txt", "a")
        arquivo_categorias.close()
        arquivo_categorias = open("categorias.txt", "r")
        arquivo_lido = arquivo_categorias.readlines()
        arquivo_categorias.close()
        for item in arquivo_lido:
            lista_exibir.insert(END, item)
        lista_exibir.place(height= 200, x = 100, y = 150)

    def incluir_categoria():
        nome = str(nome_categoria.get())
        lista_exibir.insert(END, nome)
        arquivo_categorias = open("categorias.txt", "a")
        arquivo_categorias.write(nome + ' \n')
        arquivo_categorias.close()
        exibir_atualizacao()

        
    def excluir_categoria():
        nome = str(nome_categoria.get() + ' \n')
        # faz a leitura do arquivo
        arquivo_categorias = open("categorias.txt", "r")
        arquivo_lido = arquivo_categorias.readlines()
        arquivo_categorias.close()
        # verifica se tem o nome dentro do arquivo
        # e se tiver apaga
        if nome in arquivo_lido:
            arquivo_lido.remove(nome)
        # se apagou ou nao apagou, reescreve tudo no arquivo
        arquivo_categorias = open("categorias.txt", "w")
        arquivo_categorias.writelines(arquivo_lido)
        arquivo_categorias.close()
        # tem que exibir a atualização na tela
        exibir_atualizacao()

    def entrar_categoria():
        nome = str(nome_categoria.get() + ' \n')
        arquivo_categorias = open("categorias.txt", "r")
        arquivo_lido = arquivo_categorias.readlines()
        arquivo_categorias.close()
        if nome in arquivo_lido:
            categoria = (str(nome[0:-2]) + '.txt')
            arquivo_categorias = open(categoria, 'a')
            arquivo_categorias.close()
            janela3(categoria)

    def pegar_categoria():
        nome = lista_exibir.get(ACTIVE)
        nome_categoria.insert(0, nome[0:-2])

    # Botões #

    botao_incluir = Button(janela2, text='INCLUIR', command=incluir_categoria)
    botao_incluir.place(x=100, y=520)

    botao_excluir = Button(janela2, text='EXCLUIR', command=excluir_categoria)
    botao_excluir.place(x=343, y=520)

    botao_entrar = Button(janela2, text='ENTRAR', command=entrar_categoria)
    botao_entrar.place(x=230, y=520)

    botao_pegar = Button(janela2, text='PEGAR', command=pegar_categoria)
    botao_pegar.place(x=230, y=415)

    # Faz A Janela Rodar #
    
    janela2.mainloop()
