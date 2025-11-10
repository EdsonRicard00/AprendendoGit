# if é o comando "=SE do execel "
# ou seja ele é um comando de condições 

#verificar a idade 
idade =  int(input('QUal é a sua idade?'))

if idade  >= 18:
   #indentação 
    print('você é maior de idade')
else:
    print ('você é menor de idade')

  #o comando ele quer dizer 

  #prova de soft skills 
  #nota A  - 9 ou 10
  #nota B  - 8 ou 7 
  #nota C  - 6 ou 5
  #nota D  - 4 ou menor 

nota1 = int(input('Qual a nota 1?'))
nota2 = int(input('Qual é  a nota 2?'))
nota3 = int(input('Qual é a nota 3?'))

media = (nota1+nota2+nota3)/3

if media > 10:
    print("Error ao informae as notas")
elif media >= 9:
    # o comando elif é ultilizado quando temos mais que duas repostas possiveis para um if 
    print("Nota A")
elif media >= 7:
    print("Nota B")
elif media >= 5:
    print("nota C ")
else:
    print("nota D")