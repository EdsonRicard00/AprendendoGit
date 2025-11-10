# comando de repetir 
# while == enquanto 

idade = 17
while idade <18 :
   print("você é menor de idade")

 # tatica do incremento 
   idade = idade + 1
pergunta = input('digite Sim para sair')
    # o simbolo != quer dizer diferente ou negar
while pergunta != "sim":
    pergunta = input("você digitou errado, digite mais uma vez")
    break
#comando break faz o sistema para tambem 

# converter tudo para minusculo 

palavra = input("digite uma palavra tudo em maisculo")

print(palavra.lower())
# o comando lower () deixa todo o conteudo da variavel minusculo 

palavra2 = input("para finalizar o sitema digite sair ou finalizar")

while palavra2.lower() == "sair" or palavra2.lower() == "finalizar":
  print("sistema finalizado")

  print('você digitou errado, mas acabou o exemplo')
  