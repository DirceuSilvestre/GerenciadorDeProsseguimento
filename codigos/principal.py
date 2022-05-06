from tkinter import *
from tkinter.font import BOLD
from segundajanela import janela2
import time

def segunda_janela():
    
    janela.destroy()
    time.sleep(0.1)

    janela2()
    
janela = Tk()
janela.title("Gerenciador de Prosseguimento")
janela.geometry("500x600")

# Labels #
lab_inicial = Label(janela, text="Gerenciador de Prosseguimento", font=('Times New Roman', 27, BOLD))
lab_inicial.pack(side='top')

texto = Label(janela, text="""Sistema feito para gerenciar seu estudo \n e entretenimento. \n Salve onde parou e consulte depois. \n Inclua, exclua ou altere qualquer obra. \n Gerencie as obras por suas respectivas categorias, \n como Serie, Aula, Livro, Quadrinho, e etc. \n Aproveite!""", font=('Comic Sans',16))
texto.place(x=00, y=165)

botao_entrar = Button(janela, text='ENTRAR', font=80, command=segunda_janela)
botao_entrar.place(width=130, height=60, x=185, y=500)

janela.mainloop()
