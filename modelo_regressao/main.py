# importar as bibliotecas para o sistema 
#biblioteca de inteligencia artificial 

from sklearn.linear_model import LinearRegression

#a inteligencia artificial não trabalha sozinha 
#ela depende de ferramentas para tratar os dados 
import pandas as pd 
#pandas para ler os dados 
import matplotlib.pyplot as plt 
#para mostrar os dados 


#Entrada de dados - ler os dados 
#processamento de dados - interpretar eles 
#saida de dados _ exibição das informações 

#1 Ler 
df_dados = pd.read_csv("dados.csv")
print(df_dados)
print(df_dados.head()) #exibe as 5 linhas

# 2 - Processar os Dados 

#var independente 
x_independente = df_dados[["horas_estudo"]]

# var dependente 
y_dependente = df_dados[["nota"]]

#2 - Criar um modelo de regressão Linear 
modelo = LinearRegression()

# 2 - treinar  Modelo 
modelo.fit(x_independente, y_dependente)

# 2 - exibir os dados 
print("coeficiente", modelo.coef_[0]) # inclinação 
print("interceptação", modelo.intercept_)
#onde os pontos se encontram 

# 3 -  SAIDA DE DADOS   
# 3 - o que eu quero prever ?
nova_hora = [[9]] # anota o que quer preverr

#vou prever 
prever = modelo.predict(nova_hora)

#mostrar a previsão 
print ('se você estudar ', nova_hora, 'sua nota vai ser de ', prever)
#SEMPRE A REGRESÃO LINEAR OU SEJA A PREVISÃO DEVE TER DOIS GRAFICVOS EM UM SENDO ELES 
#O GRAFICO DE DISPERSÃO COM O GRAFICO  DE LINHA 
plt.plot(df_dados["horas_estudo"], modelo.predict(x_independente))
plt.scatter(df_dados["horas_estudo"], df_dados["nota"])

plt.show()