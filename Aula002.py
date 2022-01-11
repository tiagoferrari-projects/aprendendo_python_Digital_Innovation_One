a = int(input('Entre com o Primeiro valor: '))
b = int(input('Entre com o Segundo valor: '))
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

# conversao
# print('Soma: {}'. format(soma))
# print('Soma: ' + str(soma))
# print(soma)

print('Soma: {} '
      '\nSubtração: {} '
      '\nMultiplicação: {} '
      '\nDivisão: {} '
      '\nResto: {}'
      .format(soma, subtracao, multiplicacao, int(divisao), resto))

# print('Soma: {soma} '
#       '\nSubtração: {sub} '
#       '\nMultiplicação: {mult} '
#       '\nDivisão: {div} '
#       '\nResto: {resto}'
#       .format(soma=soma, sub=subtracao, mult=multiplicacao, div=divisao, resto=resto))

# conversao
# x = '1'
# soma2 = int(x) + 1
# print(soma2)
