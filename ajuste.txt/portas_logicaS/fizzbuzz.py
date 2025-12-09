# autor: Edson
# projeto : FizzBuzz
# versão :v1
# descrição: o fizzbuzz é um exercicio que imprime numeros de 1 a 100
# sempre que o numero é multiplo de 3 ele imprime "Fizz" sempre que é multiplo de 5 ele imprime "buzz"
#e se for multiplo de 3 e 5 imprime "Fizzbuzz"

numero = 1


# FIZZBUZZ  usando while 
while numero <= 100:
    if numero % 3 ==0:
        if numero % 5 == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif numero% 5 == 0:
        print("BUzz")
    else:
        print(numero)
    numero = numero + 1
print("")
print("")
print("\n\n----fim----")

#--- FizzBuzz usando FOR 
#para cada elemento entre 1 e 100
for i in range(1,101):
    #se o resto da divisao de i por 3 for zero e o resto da divisão de i por 5 tambem for zero faça 
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz- modo for")
    elif i % 3 == 0:
        print("fiZZ- modo for")
    elif i % 5 == 0:
        print("Buzz- modo for")
    else:
        print(i)

#----- informe de um numero
fizzbuzz = int(input("informe um numero"))

if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
    print("fizzbuzz")
elif fizzbuzz % 3 == 0:
    print("fizz")
elif fizzbuzz % 5 == 0:
    print('buzz')
else:
    print(fizzbuzz)