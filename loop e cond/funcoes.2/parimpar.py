# quais são os operadores matematicos da informatica?
# soma +
#subtração -
#multiplicação *
# divisão /

#criar o jogo par ou impar unsando if 
#regras 
#perguntar ao usuario dois numeros 
#somar esses dois numeros 
#aplicar operação % para descobrir o resto 
#se o resto for 0 é par 
# se não é impar 

#jogo par e impar 

numero1 = int(input("qual o numero 1?"))
numero2 = int(input("qual o numero 2?"))

soma  = numero1 + numero2

resto = soma % 2
if resto == 0:
    print("numeroo par")
else:
    print("numero impar")
    

          