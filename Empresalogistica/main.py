import tkinter as tk
#TK inter é uma biblioteca de interface para pyton.
from tkinter import ttk
#o ttk é os widgets do python, coisas que posso interagir. 

#vamos criar a nossa tela / root é o usuario principal do sitema 
root = tk.Tk() #criar uma tela principal do sistema 

root.title("Projeto scrum - Logistica")

#criar o tamanho da tela:
root.geometry("400x300") #sempre larguraXaltura é o contato do pixels. 

#______CABEÇALHO_______
cabecalho = ttk.Label(
    #qual tela vai ser 
    root, 
    #qual informação 
    text="Logistica Alpha",
    #qual a fonte
    font=("Arial",20,"bold")
)

#____________________FIM DO CABEÇALHO____________

#para ver a tela :

root.mainloop()