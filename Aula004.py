a = float(input('Primeiro bimestre: '))
while a > 10:
	a = int(input('Você digitou errado. Primeiro Bimestre: '))

b = float(input('Segundo bimestre: '))
while b > 10:
	b = int(input('Você digitou errado. Segundo Bimestre: '))

c = float(input('Terceiro bimestre: '))
while c > 10:
	c = int(input('Você digitou errado. Terceiro Bimestre: '))

d = float(input('Quarto bimestre: '))
while d > 10:
	d = int(input('Você digitou errado. Quarto Bimestre: '))

media = (a + b + c + d) / 4

print('Média: {}'.format(media))

#----------------------------------------------------
# nota = int(input('Entre com a nota: '))
# while nota >10:
#     nota = int(input('Nota inválida.\nEntre com a nota correta: '))

#---------------------------------------------------
# a = 0
# while a <= 10:
#     print(a)
#     a += 1
#
#---------------------------------------------------

# a = int(input('Entre com um número: '))
#
# div = 0
# for x in range(1, a + 1):
#     resto = a % x
#     print(x, resto)
#     if resto == 0:
#         div += 1
#
# if div == 2:
#     print('Número {} é primo.'.format(a))
# else:
#     print('Número {} NÃO é primo.'.format(a))
