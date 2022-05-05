from tkinter import *
from terceirajanela import janela3

def janela2():
    janela2 = Tk()
    janela2.title("Gerenciador de Prosseguimento")
    janela2.geometry("500x600")

    # Labels #
    lab_secundaria = Label(janela2, text="Categoria", font=('Times New Roman', 40))
    lab_secundaria.pack(side='top')

    lista_exibir = ()

    #---------------- Função ------------------#
    #
    #   conectar no sql, verificar se há tabelas
    #   se houver tabelas retornar a quantidade
    #   se não houver retorna 0
    #   faz um for que cria um botão para cada nome de tabela
    #   cada botão chama a terceira janela
    #   e passa o nome da categoria como argumento
    #
    #   Esse é objetivo, porém inicialmente farei uma lista
    #   e escrito e lido de arquivos txt
    #   fica a parte de cima para futuras melhorias
    #   assim como as imagens
    #

    # Arquivos #

    # se nao tiver arquivo cria um novo, se tiver faz a leitura
    arquivo_categorias = open("categorias.txt", "a")
    arquivo_categorias.close()
    # fecha o arquivo
    # depois abre pra ler pois o ponteiro estará na primeira linha
    arquivo_categorias = open("categorias.txt", "r")

    # le o arquivo e verifica o que tem dentro
    # se nao tiver, imprime uma mensagem na tela e fecha o arquivo
    if arquivo_categorias.read() == '':
        texto = Label(janela2, text='Ainda não há categorias \n Crie uma categoria com o botão INCLUIR ', justify=CENTER, font=30)
        texto.place(x=100, y=200)
        arquivo_categorias.close()

    # se tiver algo dentro, mostra na tela em formato de lista
    else:
        arquivo_categorias = open("categorias.txt", "r")
        arquivo_lido = arquivo_categorias.readlines()
        lista_exibir = Listbox(janela2, font=('Comic Sans', 20))
        for item in arquivo_lido:
            lista_exibir.insert(END, item)
        lista_exibir.place(height= 200, x = 100, y = 150)
        arquivo_categorias.close()
    
    
    # Funções dos Botões #
    def incluir_categoria():
        arquivo_categorias = open("categorias.txt", "a")
        arquivo_categorias.close()
        arquivo_categorias = open("categorias.txt", "a")
        arquivo_categorias.write(str(nome_categoria.get() + ' \n'))
        arquivo_categorias.close()
        lista_exibir = Listbox(janela2, font=('Comic Sans', 20))
        arquivo_categorias = open("categorias.txt", "r")
        arquivo_lido = arquivo_categorias.readlines()
        for item in arquivo_lido:
            lista_exibir.insert(END, item)
        lista_exibir.place(height= 200, x = 100, y = 150)
        arquivo_categorias.close()
        
        
        

    def excluir_categoria():
        categoria = str(nome_categoria.get() + ' \n')
        arquivo_categorias = open("categorias.txt", "r")
        arquivo_lido = arquivo_categorias.readlines()
        arquivo_categorias.close()
        if categoria in arquivo_lido:
            arquivo_lido.remove(categoria)
        lista_exibir = Listbox(janela2, font=('Comic Sans', 20))
        for item in arquivo_lido:
            lista_exibir.insert(END, item)
        lista_exibir.place(height= 200, x = 100, y = 150)
        arquivo_categorias = open("categorias.txt", "w")
        arquivo_categorias.writelines(arquivo_lido)
        arquivo_categorias.close()

    def entrar_categoria():
        categoria = str(nome_categoria.get() + ' \n')
        arquivo_categorias = open("categorias.txt", "r")
        arquivo_lido = arquivo_categorias.readlines()
        arquivo_categorias.close()
        if categoria in arquivo_lido:
            categoria = (str(categoria[0:-2]) + '.txt')
            arquivo_categorias = open(categoria, 'a')
            arquivo_categorias.close()
            janela3(categoria)
        
    def pegar_categoria():
        nome = lista_exibir.get(ACTIVE)
        nome_categoria.insert(0, nome[0:-2])
        


    # Botões #

    #botão incluir
    botao_incluir = Button(janela2, text='INCLUIR', command=incluir_categoria)
    botao_incluir.place(x=100, y=520)

    #botão excluir
    botao_excluir = Button(janela2, text='EXCLUIR', command=excluir_categoria)
    botao_excluir.place(x=343, y=520)

    #botão entrar
    botao_entrar = Button(janela2, text='ENTRAR', command=entrar_categoria)
    botao_entrar.place(x=230, y=520)

    #botão pegar
    botao_pegar = Button(janela2, text='PEGAR', command=pegar_categoria)
    botao_pegar.place(x=230, y=415)

    # Escrita #
    nome_categoria = Entry(janela2, bd=2, font=("Calibri", 15), justify=CENTER)
    
    nome_categoria.place(width=300, height=40, x=100, y=460)

    janela2.mainloop()
