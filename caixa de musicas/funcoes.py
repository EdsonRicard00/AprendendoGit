#para eu ler uma base de dados precisa importar um modulo que lê

import csv


# agora vou dizer onde está o arquivo que vou ler 
# digo o caminho (path) do arquivo 

caminho_arquivo = "C:/Users/edrpj/OneDrive/Área de Trabalho/comandos.git/musicas/assets/musicas.csv"

#sempre que eu quero criar hma função eu coloco a instrução de "def"+ o nome da funçao():
def ler_musicas():
    print("----LISTA DE MUSICAS------")
    try:
        #o comando try serve para o sistema tentar executar uma ou mais instruções se der certo ok ,mas se não der certo ele exibe a mensagem de error
        with open(caminho_arquivo,"r",encoding='utf-8') as arquivo_musica:
            #o comando with open permite que eu abra algo mas para isso devo informar
            # 1 - onde está 
            # 2 - o modo abertura (ler - r; adicionar - a,reescrever - w )
            # 3 - Não obrigatorio - colocar como quer ler(codificação)  e depois da um apelido para essa instrução.
            leitor =  csv.reader(arquivo_musica)
            #chamei um leitor para o sistema que lê csv e adicionei o método reader para ler o arquivo 
            next(leitor)
            #o comando next é para pular a primeira linha do arquuivo.

            # agora quero exbir linha por linha o leitor viu
            for cada_linha in leitor:
                if cada_linha:
                    titulo,artista,ano,genero,duracao_segundos = cada_linha
                    # tenho que falar todo cabeçalho  do meu aquivo
                    print('Artista',artista,'ano',ano)
    except FileExistsError:
        print('Error')