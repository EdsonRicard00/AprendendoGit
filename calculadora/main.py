from funcoes import *
# * = all = tudo 
def menu():
    print('GenCalc')
    print('1 - Somar')
    print('2 - Subtrair')
    print('3 - Multiplicar')
    print('4 - Dividir')
    print('5 - Potência')
    print('6 - Raiz')
    print('Qualquer outro dígito - Sair')


#vou criar a função principal de TODO sistema 
if __name__ == "__main__":
# O if __name__ = "__main__" garante que o codigo só rode quando você executar o main.py 
    menu()
    opcao = input ("Escolha uma opção no Menu ")

    num1 = float(input("digite o numero 1 = "))
    num2 = float(input("digite o numero 2 = "))

    if opcao == "1":
        print(soma(num1,num2))
    elif  opcao == "2":
        print(subtracao(num1,num2))
    elif  opcao == "3":
        print(mulltiplicacao(num1,num2))
    elif opcao == "4":
        print(divisao(num1,num2))
    elif opcao == "5":
        print(potencia(num1,num2))
    elif opcao == "6":
        print(raiz(num1,num2))
    else:
        print('thau')