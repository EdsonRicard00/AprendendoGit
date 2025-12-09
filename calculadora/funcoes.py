def soma(num1,num2):
    return num1 + num2
#o return é pareciso com o print ele retorna a inforamção da função


def subtracao(num1,num2):
    return num1 - num2

def mulltiplicacao (num1 , num2):
    return num1 * num2

def divisao(num1 , num2):
    if num2 == 0 :
        return "Error , não posso dividir por 0)"
    return num1/num2

def potencia (num1, num2):
    return num1 ** num2

def raiz (num1, num2):
    if num2 < 0:
        return "error ao calcular"
    return num1 **(1/num2)