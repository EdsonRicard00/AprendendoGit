# as portas logicas são divididas 3 para python
# porta NOT -negar alguma informação (não)
# porta para uma OR - porta de condição (ou )
#porta do AND - porta de condição (e)

#exemplos 

a = True
b = False

#seja variavel a ou b  pode haver varios reulsultados
print("NOT A:", not a )
# em alguns momentoss eu posso usar o operador != para falar que é diferente 

#porta or 
print("a ou b ", a or b )

# porta do and 
print("a e b ",a and b )

#-------------- exemplo de como usar AND -----------------------

idade = 16
carteira = False

# enquanto for menor de idade e não tiver carteira o sistema pergurnta
#se eu fiz aniversario e se eu tirei a carteira 
#quando eu tiver idade + carteira ele fala que eu posso dirigir

while idade < 18 or carteira == False:
    pergunta_aniversario = input('você ja fez aniversario?')
    if pergunta_aniversario.lower() == 'sim':
        idade = idade + 1
        print("parabens, então você tem ",idade )
        pergunta_carteira = input('você tirou carta?')
    if pergunta_carteira.lower() == "sim":
        carteira = True

print("pode dirigir")