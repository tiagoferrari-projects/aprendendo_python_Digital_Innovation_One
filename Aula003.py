a = float(input('Primeiro bimestre: '))
if a > 10:
	a = int(input('Você digitou errado. Primeiro Bimestre: '))

b = float(input('Segundo bimestre: '))
if b > 10:
	b = int(input('Você digitou errado. Segundo Bimestre: '))

c = float(input('Terceiro bimestre: '))
if c > 10:
	c = int(input('Você digitou errado. Terceiro Bimestre: '))

d = float(input('Quarto bimestre: '))
if d > 10:
	d = int(input('Você digitou errado. Quarto Bimestre: '))

media = (a + b + c + d) / 4

print('Média: {}'.format(media))

#if a <= 10 and b <= 10 and c <= 10 d <= 10
#	print('Média {}'.format(media))
#else:
#	print('Foi informado alguma nota errada')
#--------------------------------------------------------
#a = int(input('Entre com o Primeiro valor: ')
#a = int(input('Entre com o Segundo valor: ')
#
#resto_a = a % 2
#resto_b = b % 2
#
#if resto_a == 0 or resto_b == 0:
#	print('Foi digitado um número par')
#else:
#	print('Nenhum par foi digitado')
#
#if resto == 0:
#	print('Número é par')
#else:
#	print('Número é ímpar')
#
#-------------------------------------------------------
#Operador not inverte o resultado da condição
#
#-------------------------------------------------------
#a = int(input('Primeiro valor: '))
#b = int(input('Segundo valor: '))
#c = int(input('Terceiro valor: '))
#
#if a > b and a > c:
#	print('O Maior número é {}'.format(a))
#elif b > a and b > c:
#	print('O Maior número é {}'.format(b))
#else:
#	print('O Maior número é {}'.format(c))
#print('Final do Programa')
