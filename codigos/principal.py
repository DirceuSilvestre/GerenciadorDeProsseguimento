from tkinter import *
from segundajanela import janela2
import time

def segunda_janela():
    
    janela.destroy()
    time.sleep(0.1)

    janela2()
    
janela = Tk()
janela.title("Gerenciador de Prosseguimento")
janela.geometry("500x600")

# Importar Imagens #
imagem_inicial = PhotoImage(file="imagens\\TelaInicial.png")
imagem_entrar = PhotoImage(file="imagens\\Entrar.png")

# Labels #
lab_inicial = Label(janela, image=imagem_inicial)
lab_inicial.pack()

botao_entrar = Button(janela, bd=0, image=imagem_entrar, command=segunda_janela)
botao_entrar.place(width=187, height=56, x=157, y=522)

janela.mainloop()
