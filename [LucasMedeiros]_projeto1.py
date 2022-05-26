import json
import os.path
import sys

def obter_dados():
    '''
    Essa função carrega os dados dos produtos e retorna uma lista de dicionários, onde cada dicionário representa um produto.
    NÃO MODIFIQUE essa função.
    '''
    with open(os.path.join(sys.path[0], 'dados.json'), 'r') as arq:
        dados = json.loads(arq.read())
    return dados

def listar_categorias(dados: list) -> list:
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista contendo todas as categorias dos diferentes produtos.
    Cuidado para não retornar categorias repetidas.
    '''

    categorias = []

    for i in range(0, len(dados)):
        if not(dados[i]['categoria'].upper() in categorias):
            categorias.append(dados[i]['categoria'].upper())
    return sorted(categorias)

def listar_por_categoria(dados: list, categoria: str) -> list:
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar uma lista contendo todos os produtos pertencentes à categoria dada.
    '''
    lista = []

    for i in range(0, len(dados)):
      if dados[i]['categoria'].upper() == categoria:
        lista.append(dados[i])
    return lista


def produto_mais_caro(dados: list, categoria: str) -> dict:
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar um dicionário representando o produto mais caro da categoria dada.
    '''

    valor_caro = 0

    for i in range(0, len(dados)):

        if float(dados[i]['preco']) > valor_caro and dados[i]['categoria'].upper() == categoria:
            valor_caro = float(dados[i]['preco'])
            produto_caro = dados[i]

    return produto_caro

def produto_mais_barato(dados: list, categoria: str) -> dict:
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar um dicionário representando o produto mais caro da categoria dada.
    '''
    cont = 0

    while cont < len(dados):
        if dados[cont]['categoria'].upper() == categoria:
            valor_barato = float(dados[cont]['preco'])
            break
        cont += 1
    for i in range(0, len(dados)):
        if float(dados[i]['preco']) < valor_barato and dados[i]['categoria'].upper() == categoria:
            valor_barato = float(dados[i]['preco'])
            produto_barato = dados[i]

    return produto_barato

def top_10_caros(dados: list) -> list:
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista de dicionários representando os 10 produtos mais caros.
    '''
    lista = sorted(dados, key = lambda x: float(x['preco']), reverse= True)[0:10]
    return (lista)

def top_10_baratos(dados: list) -> list:
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista de dicionários representando os 10 produtos mais baratos.
    '''

    lista = sorted(dados, key = lambda x: float(x['preco']))[0:10]
    return (lista)

def print_formatado(resposta: list | dict) -> None:
    '''
    O parâmetro "resposta" pode ser do tipo lista ou do tipo dicionário.
    Essa função deverá imprimir na tela os produtos, formatados com boa visualização para o usuário.
    '''

    if type(resposta) == list:
        for i in range(0, len(resposta)):
            print(f'{i + 1}. {resposta[i]}')
    else:
        print(resposta)

    print('~*' * 21 + '~')

def valida_entrada_numerica(numero: str) -> str:
    '''
    O parâmetro número deverá ser do tipo str
    Essa função deverá assegurar que o usuário optou por uma escolha correta, caso contrário solicitará um input
    até que o usuário preencha corretamente. O retorno da função é um str'''

    opcoes = ['0', '1', '2', '3', '4', '5', '6']

    if numero in opcoes:

        pass

    else:
        while not numero.isdigit() or numero not in opcoes:

            numero = input('\nVocê digitou uma opção inválida!\nQual opção você deseja escolher? ')

    return numero

def valida_entrada_categoria(categoria):
    '''
    O parâmetro número deverá ser do tipo str
    Essa função deverá assegurar que o usuário optou por uma categoria existente, caso contrário solicitará um input
    até que o usuário preencha corretamente. O retorno da função é um str'''

    opcoes = listar_categorias(dados)

    if categoria in opcoes:
        pass
    else:
        while (categoria not in opcoes):

            categoria = input('\nVocê digitou uma categoria inexistente!\nDigite uma categoria correta! ').upper()

    return categoria

def menu(dados: list) -> None:
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá, em loop, realizar as seguintes ações:
    - Exibir as seguintes opções:
        1. Listar categorias
        2. Listar produtos de uma categoria
        3. Produto mais caro por categoria
        4. Produto mais barato por categoria
        5. Top 10 produtos mais caros
        6. Top 10 produtos mais baratos
        0. Sair
    - Ler a opção do usuário.
    - No caso de opção inválida, imprima uma mensagem de erro.
    - No caso das opções 2, 3 ou 4, pedir para o usuário digitar a categoria desejada.
    - Chamar a função adequada para tratar o pedido do usuário e salvar seu retorno.
    - Imprimir o retorno salvo.
    O loop encerra quando a opção do usuário for 0.
    '''

    print('''\nDigite o respectivo número para obter uma opção abaixo:
        1. Listar categorias
        2. Listar produtos de uma categoria
        3. Produto mais caro por categoria
        4. Produto mais barato por categoria
        5. Top 10 produtos mais caros
        6. Top 10 produtos mais baratos
        0. Sair\n''')

    numero = input('Qual opção você deseja escolher? ')
    print()

    while not (numero == '0'):

        numero = valida_entrada_numerica(numero)

        if numero == '2' or numero == '3' or numero == '4':

            categoria = input('\nQual categoria você deseja escolher? ').upper()

            valida_entrada_categoria(categoria)

        if numero == '1':
                resposta = listar_categorias(dados)
        elif numero == '2':
                resposta = listar_por_categoria(dados, categoria)
        elif numero == '3':
                resposta = produto_mais_caro(dados, categoria)
        elif numero == '4':
                resposta = produto_mais_barato(dados, categoria)
        elif numero == '5':
                resposta = top_10_caros(dados)
        elif numero == '6':
                resposta = top_10_baratos(dados)

        print_formatado(resposta)

        numero = input('\nQual opção você deseja agora? ')
    print('\nObrigado por usar o nosso programa! FIM!')

2# Programa Principal - não modificar!
dados = obter_dados()
menu(dados)