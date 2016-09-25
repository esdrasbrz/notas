"""
Arquivo principal que irá manipular a estrutura e realizar as operações necessárias
"""

from acoes import *
from estrutura import *

# Função principal
def main():
    bd = BD() # instancia da base de dados total

    print("Lendo base de dados...")
    bd.abrir()

    opcoes = menu()

    # loop para receber as ações
    while True:
        print()
        opcao = input("O que deseja fazer? ")

        try:
            # chama a função mapeada
            opcoes[opcao.upper()](bd)

            print()
            input("Pressione 'enter' para continuar...")
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
        'IS': new_semestre,
        'ID': new_disciplina,
        'IT': new_teste,
        'IN': set_nota,
        'RS': del_semestre,
        'RD': del_disciplina,
        'RT': del_teste,
        'ED': estat_disciplina,
        'ES': estat_semestre,
        'S': salvar,
        'Q': sair,
    }

    # imprime o menu estilizado :)
    print()
    print("-------------------")
    print("| Menu Principal: |")
    print("-------------------")
    print()

    print("Inserir Semestre: IS")
    print("Inserir Disciplina: ID")
    print("Inserir Teste: IT")
    print("Inserir Nota: IN")
    print("Remover Semestre: RS")
    print("Remover Disciplina: RD")
    print("Remover Teste: RT")
    print("Estatísticas por Disciplina: ED")
    print("Estatísticas por Semestre: ES")
    print("Salvar Alterações: S")
    print("Sair: Q")

    return opcoes

if __name__ == '__main__':
    main()
