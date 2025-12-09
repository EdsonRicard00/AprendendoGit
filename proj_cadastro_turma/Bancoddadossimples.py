#uma lista é uma variavel quee suporta muitos dados 

Frutas = []
# quando coloco a lista apenas  [], eu estou dizendo que ela eé vazia.
print(Frutas)
print("[]")

#o usuario pode adicionar
#o usuario pode excluir a fruta
#o usuario pode ver a lista
#o usuario pode sair

print('----Bem vindo ao varejo Gen ----')
print('suas opçoes são:')
print('1 - add fruta')
print('2 - excluir fruta')
print('3 - ver lista')
print('4 - sair')

escolha =  int(input('qual a opção desejada?'))
if escolha< 1 or escolha > 4:
    print('escolha não reconhecida, finalizando o sistema')
else:
    while escolha >= 1:
        #caso 1 - add
        if escolha == 1 :
            nova_fruta = input ('qual fruta que adicionar ')
        #para adicionar um elemento lista eu devvo chamar a lista e dar o atributo append anexando assim , o novo valor 
            Frutas.append(nova_fruta)
            print('fruta',Frutas[-1],' adicionado com sucesso')
            escolha =  int(input('qual a opção desejada?'))
        # caso 2 - excluir 
        elif escolha == 2:
            for posicao , cada_fruta in enumerate(Frutas, start=1):
                print(posicao," - ", cada_fruta)
            print('agora vocêe pode excluir um produto')
            posiçao_fruta = int(input('digite a posiçao da fruta'))
            Frutas.pop(posiçao_fruta-1)
            # o comando pop é para excluir um intem da lista
            print ('fruta excluida com sucesso')
            escolha =  int(input('qual a opção desejada?'))
        
        # caso 3 - ver lista
        elif escolha == 3:
            for nome_fruta in Frutas:
                print(nome_fruta)
            escolha =  int(input('qual a opção desejada?'))
        # Caso 4 - sair
        elif escolha == 4:
            print('Thau')
            break