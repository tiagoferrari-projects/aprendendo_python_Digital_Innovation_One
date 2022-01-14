lista = [12, 10, 5, 7]
lista_animal = ['lobo', 'cachorro', 'gato', 'elefante', 'arara']

# -------------------------------------TUPLAS ----------------------------- #
# tuplas são imutáveis, não consigo alterar os valores
# listas são mutáveis, conseguimos manipular os elementos
lista_animal[0] = 'macaco'  # exemplo
print(lista_animal)

tupla = (1, 10, 12, 14)
print(tupla[2])

# print(len(tupla)) # len informa quantos registros tem tanto na tupla quanto na lista também pode ser usado
# print(len(lista_animal))

# converte lista em tupla
tupla_animal = tuple(lista_animal)
print(type(tupla_animal))
print(lista_animal)

# converte tupla em lista
lista_numerica = list(tupla)
print(type(lista_numerica))
print(lista_numerica)
# --------------------------LISTA ---------------------------------- #
# print(lista_animal[1])

# # sorte ordena os elementos
# lista.sort()
# lista_animal.sort()
# print(lista)
# print(lista_animal)

# # ordena de maneira reversa
# lista_animal.reverse()
# print(lista_animal)
#-----------------------------
# soma = 0
# for x in lista_animal:
#     print(x)
#-----------------------------

# soma = 0
# for x in lista:
#     print(x)
#     soma += x
# print(soma)
#-----------------------------

# print(sum(lista)) # soma todos os valores de Lista
# print(max(lista)) # mostra o maior valor de lista
# print(min(lista)) # mostra o menor valor de lista
#
# print(max(lista_animal)) # busca gato porque começa com 'g' que seria letra maior
# print(min(lista_animal)) # busca cachorro porque começa com 'c' que seria letra menor
#----------------------------------------------------------------------------------------

# busca se o valor está na lista
# if 'lobo' in lista_animal:
#     print('Existe lobo na lista')
# else:
#     print('Não existe lobo na lista')
#-----------------------------------------------------------------------------------------

# nova_lista = lista_animal * 3 # multiplica a lista para imprimir 3 vezes
# print(nova_lista)

# if 'lobo' in lista_animal:
#     print('Existe lobo na lista')
# else:
#     print('Não existe lobo na lista.\nAdicionando...')
#     lista_animal.append('lobo')  # append adiciona novos registros a lista
#     print(lista_animal)

# retira o último elemento da lista
#lista_animal.pop()
#---------------------------------------
#retirou o cachorro
# lista_animal.pop(0)
# print(lista_animal)
#---------------------------------------
# remove um elemente que eu já conheço
# lista_animal.remove('elefante')
# print(lista_animal)
