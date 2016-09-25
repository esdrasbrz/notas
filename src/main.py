"""
Arquivo principal que irá manipular a estrutura e realizar as operações necessárias
"""

from acoes import *

# Função principal
def main():
    opcoes = menu()

    # loop para receber as ações
    while True:
        print()
        opcao = input("O que deseja fazer? ")

        try:
            # chama a função mapeada
            opcoes[opcao.upper()]()
        except KeyError:
            print("Não sei fazer isso, desculpe :(")

        menu()

"""
Imprime o menu oferecendo as opções para manipular a base de dados e retorna o dicionário
com as opções e as funções mapeando cada uma
"""
def menu():
    # dicionário com as opções
    opcoes = {
        'S': sair,
    }

    # imprime o menu estilizado :)
    print()
    print("-------------------")
    print("| Menu Principal: |")
    print("-------------------")
    print()

    print("Sair: S")

    return opcoes

if __name__ == '__main__':
    main()
