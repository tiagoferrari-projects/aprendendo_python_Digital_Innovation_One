from datetime import date, time, datetime, timedelta


def trabalhando_com_date():
    # informa data atual já formatado em pt-br
    data_atual = date.today()
    # print(data_atual.strftime('%d-%m-%Y'))
    data_atual_str = data_atual.strftime('%A - %B - %Y')
    print(type(data_atual))
    print(data_atual_str)
    print(type(data_atual_str))


def trabalhando_com_time():
    horario = time(hour=15, minute=18, second=30)
    # print(horario)
    horario_str = horario.strftime('%H:%M:%S')
    print(horario_str)


def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)
    # print(data_atual.strftime('%d/%m/%Y %H:%M:%S'))
    print(data_atual.strftime('%c'))
    print(data_atual.weekday())

    tupla = ('Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado')
    print(tupla[data_atual.weekday()])
    data_criada = datetime(2022, 1, 4, 00, 30, 2)
    print(data_criada)
    print(data_criada.strftime('%c'))

    data_string = '01/01/1994 00:32:03'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y %H:%M:%S')
    print(data_convertida)
    nova_data = data_convertida - timedelta(days=365, hours=2, minutes=15)
    print(nova_data)


if __name__ == '__main__':
    # trabalhando_com_date()
    trabalhando_com_time()
    trabalhando_com_datetime()
