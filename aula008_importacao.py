# importando classes diretamente de outros módulos
from aula007_televisao import Televisao
from aula007_calculadora1 import Calculadora
# importando méto tambem diretamente
from aula008_contador_letras import contador_letras,teste

if __name__ == '__main__':

    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)

    calculadora = Calculadora(28, 7)
    print(calculadora.soma())

    lista = ['cachorro', 'gato', 'elefante']
    total_letras = contador_letras(lista)
    print('Total de letras por palavra da lista: {}'.format(total_letras))
    print(teste())
