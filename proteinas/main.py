from funcoes import *

while True:
    menu()
    opcao = int(input("escolha a opção"))

    if opcao == 1:
        menu_objetivo()
        objetivo = int(input("qual seu obejetivo ??"))
        peso = float(input("qual seu peso (KG)"))

        resultado_proteinaas = calc_proteinas (peso, objetivo)
        print("você precia de ", round(resultado_proteinaas,2))

    elif opcao == 2:
        peso = float(input("qual seu peso(kg)"))
        altura = float(input("Qual é sua altura  em metros"))

    if opcao == 1:
        resultado_imc = calc_imc(peso, altura)
        print('Seu IMC é de', resultado_imc)
    else:
        print("tchau")
        break

