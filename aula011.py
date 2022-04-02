""" tratamento de exceção
ZeroDivisionError é uma classe que já vem do builtin do python
BaseException é o pai de todas as exceções, a primeira exceção
else: executa código quando não tem exceção
no finallytodo código será executado, dando erro ou não """

lista = [1, 10]
try:
    arquivo = open('teste.txt', 'r')
    texto = arquivo.read()
    divisao = 10 / 1
    numero = lista[3]
    # x = a
except ZeroDivisionError:
    print('Não é possível realizar uma divisão por 0.')
except ArithmeticError:
    print('Houve um erro ao realizar uma operação aritmética.')
# erro genérico
# except:
#     print('Erro desconhecido!')
except IndexError:
    print('Erro ao acessar um índice inválido da lista!')
except Exception as ex:
    print('Erro desconhecido. Erro: {}'.format(ex))
# exceção filha primeiro depois da exceção Pai
# except BaseException as ex:
    # print('Erro desconhecido. Erro: {}'.format(ex))
else:
    print('Excuta quando não ocorre exceção')
finally:
    print('Sempre executa')
    print('fechando arquivo')
    arquivo.close()
