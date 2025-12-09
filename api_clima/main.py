#aquele link da api = endpoint
#endpint é o link para os métodos get post
# ex : https://api.open-meteo.com/v1/forecast

# sempre que uso api em python , devo chamar a biblioteca de requisiçoes
#pip install requests 
#sempre que queremos  mostrar graficos , podemos usar a biblioteca 
#pip install requests 
#pip install matplotlib

import requests

import matplotlib.pyplot as plt


#criar uma funçao chamada de buscar_clima 

def buscar_clima(latitude, longitude):
    #deve informar o endpoint
    endepoint = 'https://api.open-meteo.com/v1/forecast'
    # informar os parametros para o sitema em formato de dicio.
    ## dicionario trabalha com chave:valor
    parametros = {
        # "chave" valor,
        "latitude": latitude,
        "longitude" : longitude,
        "hourly":"temperature_2m",
        "timezone" : "America/Sao_Paulo"
    }
    repostas = requests.get(endepoint,params=parametros)
    # sempre que queremos obter a resposta usamos o comando
    #requests.get para pegar os valores e colocamos os atributos
    #requests.get(variavek_do_endpoist, parms= dicionario _cin_parametros)

    #para o sistema usar o método post - para mostrar as informações 
    dados = repostas.json()
    # o sistemaa tranforma os dados em json para poder manipular eles
    return dados


latitude = float (input("informe a latitude"))
longitude =float (input("informe a longitude"))
dados = buscar_clima(latitude, longitude)
# vamos começar a exbir informaçoes para os usuarios 
horas = dados['hourly']['time']
#chamo a base de dados , informo o parametro e qual a variavel que o paramentro vai ler 
temperatura = dados ['hourly'] ['temperature_2m']

plt.plot(horas, temperatura)
#plt.plot cria um grafico , onde informo o parametro primeiro e o eixo x e depois o eixo y
#plt.plot(eixo_x, eixo_y)
plt.title('TEMPERATURA POR HORA')
#PARA ver o grafico 
plt.show()



