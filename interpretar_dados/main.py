import pandas as pd
#import = chamar a biblioteca para o sistema 
# o nome da bibliotecca 
# as blábláblá - para apelidar a biblioteca 

# df quer dizer data g=frame 
df_alunos = pd.read_csv("interpretar_dados/alunos.csv", sep=',', encoding='utf-8')
#pd.read_csv - faz com que o pandas leia o arquivo csv para python 
#no caso o separador ,  você arruma o que precisarr com o aargumento sep= ''

print(df_alunos)
# add novo  valor na data frame 
# em geral o data frame tem muitos campos 
#se o phyton le o df como chave -valor - posso ultilizar dicionario para add valores 

novo_aluno = {
    "Carimbo de data/hora ":"17/11/2025 10:33:42",
    "nome":"joao",
    "cidade":"tatuepe",
    "zona":"zona leste"
}

# add o dado 
df_alunos = pd.concat([df_alunos, pd.DataFrame([novo_aluno])],ignore_index=True)

#para adicionar um novo valor devo chamar o data frame e atribuir a ele 
# a funçao concat da biblioteca(pd.concat) e chamar os atributos 
#o [meu frame e o novo dado ] = ([df_alunos, pd.DataFrame])

#salvar a info
df_alunos.to_csv("interpretar_dados/alunos.csv", index=False)

