import requests

def retorna_dados_cep(cep):
    response = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    print(response.status_code)

    # # mostra as informações em string
    # print(response.text)
    # print(type(response.text))

    # mostra as informações em json/dicionário
    print(response.json())
    print(type(response.json()))
    dados_cep = response.json()
    print(dados_cep['logradouro'])
    print(dados_cep['bairro'])
    return dados_cep


def retorna_dados_pokemon(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
    dados_pokemon = response.json()
    return dados_pokemon


def retorna_response(url):
    response = retorna_response(url)
    return response.text


if __name__ == '__main__':
    response = retorna_response('https://www.dio.me/')
    print(response)
    # retorna_dados_cep('15993646')
    # dados_pokemon = retorna_dados_pokemon('pikachu')
    # print(dados_pokemon['sprites']['front_shiny'])
