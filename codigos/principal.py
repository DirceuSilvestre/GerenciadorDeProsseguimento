from tkinter import *


if __name__ == '__main__':

    janela = Tk()
    janela.title("Gerenciador de Prosseguimento")
    janela.geometry("500x600")

    # Importar imagens #
    imagem_inicial = PhotoImage(file="imagens\\TelaInicial.png")

    # Labels #
    lab_inicial = Label(janela, image=imagem_inicial)
    lab_inicial.pack(expand=0)



    janela.mainloop()
