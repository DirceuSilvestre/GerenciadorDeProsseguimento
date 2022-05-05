from tkinter import *

def janela3(nome_categoria):
    janela3 = Tk()
    janela3.title("Gerenciador de Prosseguimento")
    janela3.geometry("500x600")

    def incluir_obra():
        pass

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