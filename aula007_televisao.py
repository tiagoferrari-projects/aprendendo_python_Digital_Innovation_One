class Televisao:
    def __init__(self):
        # instancia TV sempre desligada
        self.ligada = False
        #começa no canal 5
        self.canal = 5

    # método botão power
    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    # método aumentar os canais
    def aumenta_canal(self):
        # condição para aumentar canais caso TV esteja ligada
        if self.ligada:
            #incrementa o canal de 1 em 1
            self.canal += 1

    # método diminuir os canais
    def diminui_canal(self):
        # condição para diminuir canais caso TV esteja ligada
        if self.ligada:
            #decrementa o canal de 1 em 1
            self.canal -= 1

televisao = Televisao()

print('Televisão está ligada: {}'.format(televisao.ligada))
televisao.power()
print('Televisão está ligada: {}'.format(televisao.ligada))
televisao.power()
print('Televisão está ligada: {}'.format(televisao.ligada))

print('Canal: {}'.format(televisao.canal))
televisao.power()
print('Televisão está ligada: {}'.format(televisao.ligada))
televisao.aumenta_canal()
televisao.aumenta_canal()
print('Canal: {}'.format(televisao.canal))
televisao.diminui_canal()
televisao.diminui_canal()
televisao.diminui_canal()
print('Canal: {}'.format(televisao.canal))
