# lista [] -> colchetes
# tuplas () -> parenteses
# conjunto {} -> chaves

#-----------------------------------------------------------------------------------------------------------------------
conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}
conjunto_uniao = conjunto.union(conjunto2) # união entre os elementos do conjunto com conjunto 2, ja tirando a duplicidade
print('União: {}'.format(conjunto_uniao))

conjunto_interseccao = conjunto.intersection(conjunto2) # intersecção entre os elementos do conjunto com conjunto 2
print('Intersecção: {}'.format(conjunto_interseccao))

conjunto_diferenca1 = conjunto.difference(conjunto2) # diferença dos elementos do conjunto 1 com conjunto 2
print('Diferença entre 1 e 2: {}'.format(conjunto_diferenca1))
conjunto_diferenca2 = conjunto2.difference(conjunto) # diferença dos elementos do conjunto 2 com conjunto 1
print('Diferença entre 2 e 1: {}'.format(conjunto_diferenca2))

conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2) # dirença simétrica
print('Diferença Simétrica: {}'.format(conjunto_diff_simetrica))

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_subset = conjunto_a.issubset(conjunto_b) # verifica se conjunto_a é um subconjunto do conjunto_b
print('A é super conjunto de B: {}'.format(conjunto_subset))

conjunto_superset = conjunto_b.issuperset(conjunto_a) # verifica super conjunto
print('B é um superconnjunto de A: {}'.format(conjunto_superset))

#-----------------------------------------------------------------------------------------------------------------------
# converter lista em conjunto
# lista = ['cachorro', 'gato', 'cachorro', 'gato', 'elefante']
# print(lista)
# conjunto_animais = set(lista)
# print(conjunto_animais)
#
# lista_animais = list(conjunto_animais)
# print(lista_animais)
#-----------------------------------------------------------------------------------------------------------------------
# conjunto = {1, 2, 3, 4, 4, 2} # conjunto exclui duplicidades
# print(type(conjunto))
# print(conjunto)
# print(conjunto)
#
# conjunto.add(5) # adiciona número 5
# print(conjunto)
#
# conjunto.discard(2) # remove número 2
# print(conjunto)


