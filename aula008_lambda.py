# Lambda é uma função anônima,
# Uma forma de simplificar funções que dêem para resolver com uma linha de código
# Eventos que se repetem com frequência
contador_letras = lambda lista: [len(x) for x in lista]

lista_animais = ['cachorro', 'gato', 'elefante']
print(contador_letras(lista_animais))

soma = lambda a, b: a + b
subtracao = lambda a, b: a - b
print(soma(5, 10))
print(subtracao(10, 5))

#dicionário com funções lambda
calculadora = {
    'soma': lambda a, b: a + b,
    'subtracao': lambda a, b: a - b,
    'multiplicacao': lambda a, b: a * b,
    'divisao': lambda a, b: a / b
}

print(type(calculadora))
soma = calculadora['soma']
#soma = lambda a, b: a + b
multiplicacao = calculadora['multiplicacao']
print('A soma é : {}'.format(soma(10, 5)))
print('A multiplicação é : {}'.format(multiplicacao(10, 2)))
