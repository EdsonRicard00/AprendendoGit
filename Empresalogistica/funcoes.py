import csv
import os 
# os é as funções do sistema operacional (operational sistem )

dados_fretes = "Banco_de_dados.csv"
#dizendo o nome do arquivo 
campo_fretes = ["Registro_frete","origem","Destino","Cliente","Produto","Status"]
#importar todos os campos do frete r
#funções 
#adicionar_registo_frete - segurança para o sistema 
#abrir_o_formulario_do_frete - criar uma tela para add infos 
#salvar_o_frete - atualizar o csv
import tkinter as tk

def abrir_formulario_frete():
    popup_frete = tk.Toplevel()
    popup_frete.title("Adicionar fretes")
    popup_frete.geometry("350x300")

    label_fretes = ["Registro_frete","origem","Destino","Cliente","Produto","Status"]
    fretes = {}

    #vamos sequenciar campo com os dados 
    for campo_dados in label_fretes:
        #para cada campo que o usuario digita 
        tk.Label(popup_frete,text=campo_dados).pack(pady=5)
        #essa linha cria todos os textois para o usuario 
        entrada_fretes = tk.Entry(popup_frete)
        #entry é o input (caixa de texto )
        entrada_fretes.pack()
        fretes[campo_dados] = entrada_fretes
        
    def salvar ():
        dados = {campo_dados:fretes[campo_dados].get() for campo_dados in fretes}
        add_clientes(dados)
        # fechar automatico uma janela
        popup_cliente.destroy()  

    tk.Button(popup_cliente, text="SALVAR", command=salvar).pack(pady=20)
    tk.Button(popup_cliente, text="LIMPAR", pady=20).pack()

def add_clientes(registro_clientes):
    # para manipular o arquivo
    arquivo = os.path.isfile(dados_clientes)

    # add valores
    # smepre que usamos o with open informamos
    # 1 - arquivo, 2 - modo, 3 - novas linhas, 4 - utf-8
    with open(dados_clientes, "a", newline="", encoding="utf-8") as arquivo_clientes:
        escrever = csv.DictWriter(arquivo_clientes, fieldnames=campo_clientes)
    
        # para adicionar os dados no CSV
        escrever.writerow(registro_clientes)