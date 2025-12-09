def menu():
    print("Bem vindo ao Pretein _CALC_ GENERE")
    print("EScolha uma Opção ao seu perfil")
    print("1 - calcular proteintas")
    print("2 -  calcular IMC")
    print("Qualquer outro numero - Sair ")

#-- funçao para saber o obejetivo do usuario 
def menu_objetivo():
    print("Qual é sua Meta ideal?")
    print("1 - Perder Peso")
    print("2 - Manter peso")
    print("3 - Ganhar peso")

def calc_proteinas(peso,objetivo):
    if objetivo == 1:
        return peso * 2
    elif objetivo == 2:
        return peso * 1.6
    elif objetivo == 3:
        return peso * 1.8
    else:
        return None
    #o comando None , é para não fazer nada;

def calc_imc (peso, altura):
    return peso / (altura**2)
    
def imc(valor_imc):
    if valor_imc < 18.5:
        return "Abaixo do peso"
    elif valor_imc < 24.9:
        return "Peso normal"
    elif valor_imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidade"