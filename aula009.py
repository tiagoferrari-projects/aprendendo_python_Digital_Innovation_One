# open: abre um arquivo ou até mesmo criar e também indicar o caminho do arquivo
# se não passarmos o caminho por padrão é criado no diretório do projeto
# w = escrever no arquivo
# write cria a escrita e também sobrescreve, sempre tomar cuidado!
# a = cria e atualiza o arquivo, diferente do W que somente escreve
# r = leitura do arquivo

import shutil

def escrever_arquivo(texto):
    diretorio = '/home/tiagoferrari/Python_Dio/IntroducaoPython/teste.txt'
    arquivo = open(diretorio, 'w')
    arquivo.write(texto)
    arquivo.close()


def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()


def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)


def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    # print(aluno_nota)
    aluno_nota = aluno_nota.split('\n')
    # print(aluno_nota)
    lista_media = []
    for x in aluno_nota:
        lista_notas = x.split(',')
        # print(lista_notas)
        aluno = lista_notas[0]
        lista_notas.pop(0)
        print(aluno)
        print(lista_notas)
        media = lambda notas: sum([int(i) for i in notas]) / 4
        print('Média: {}'.format(media(lista_notas)))
        lista_media.append({aluno: media(lista_notas)})
    return lista_media


def copia_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, 'home/tiagoferrari/Python_Dio/IntroducaoPython/')


def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, 'home/tiagoferrari/Python_Dio/IntroducaoPython')


if __name__ == '__main__':
    copia_arquivo('notas.txt')
    # lista_media = media_notas('notas.txt')
    # print(lista_media)
    # escrever_arquivo('Primeira linha.\n')
    # aluno = 'Paulo,10,1,3,0\n'
    # atualizar_arquivo('notas.txt', aluno)
    # ler_arquivo('teste.txt')
