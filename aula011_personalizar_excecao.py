''' toda nota maior ou menor que 10 será feito excecao
assim como entradas que não são números
break força a saída do loop.'''


class Error(Exception):
    pass


class InputError(Error):
    def __init__(self, message):
        self.message = message


while True:
    try:
        x = int(input('Digite uma nota entre 0 e 10: '))
        print(x)
        if x > 10:
            raise InputError('Nota não pode ser maior que 10!')
        elif x < 0:
            raise InputError('Nota não pode ser menor que 0!')
        break
    except ValueError:
        print('Valor inválido. Deve-se digitar apenas número.')
    except InputError as ex:
        print(ex)
