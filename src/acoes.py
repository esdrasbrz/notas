"""
Arquivo com as ações de seleção de cada item do menu principal
"""

from estrutura import *

# Função para sair do programa
def sair(bd):
    # salva as alterações
    salvar(bd)

    print()
    print("Já estava na hora de ir estudar :D")
    exit()

# Exibe todos os semestres para o usuário selecionar
def _list_semestres(semestres):
    for i, semestre in enumerate(semestres):
        print("%d: %s" % (i, semestre))

# Exibe todas as disciplinas de um determinado semestre
def _list_disciplinas(disciplinas):
    for i, disciplina in enumerate(disciplinas):
        print("%d: %s" % (i, disciplina))

# Função para inserir um novo semestre
def new_semestre(bd):
    try:
        ano = int(input("Digite o ano: "))
        periodo = int(input("Digite o período (1 ou 2): "))

        semestre = Semestre(ano=ano, periodo=periodo)
        bd.semestres.append(semestre)

        print("Semestre inserido com sucesso!")
    except:
        print("Desculpe, algum erro ocorreu :(")


# Função para inserir uma nova disciplina
def new_disciplina(bd):
    try:
        print("A qual semestre ela pertence?")
        _list_semestres(bd.semestres)

        print()
        i = int(input("Digite o índice do semestre: "))
        nome = input("Digite o nome da disciplina: ")
        creditos = int(input("Digite quantos créditos ela possui: "))

        disciplina = Disciplina(nome=nome, creditos=creditos, semestre=bd.semestres[i])
        bd.disciplinas.append(disciplina)

        print("Disciplina inserida com sucesso!")
    except:
        print("Desculpe, algum erro ocorreu :(")

# Função para inserir um novo teste
def new_teste(bd):
    try:
        # escolhe o semestre
        print("Selecione o semestre")
        _list_semestres(bd.semestres)
        print()
        i_sem = int(input("Digite o índice do semestre: "))

        # cache na lista de disciplinas
        disciplinas = bd.semestres[i_sem].get_disciplinas(bd)
        
        # escolhe a disciplina
        print("Selecione a disciplina")
        _list_disciplinas(disciplinas)
        print()
        i_disc = int(input("Digite o índice da disciplina: "))

        # loop para cadastrar vários testes
        while True:
            print()
            nome = input("Digite o nome do teste: ")
            peso = int(input("Qual o peso? "))
            
            # instancia e insere no bd
            teste = Testes(nome=nome, peso=peso, disciplina=disciplinas[i_disc])
            bd.testes.append(teste)

            opcao = input("Deseja cadastrar mais um teste? (S/n)")
            if opcao and opcao.upper() == 'N':
                break
    except:
        print("Desculpe, algum erro ocorreu :(")

"""
Função para salvar todas as alterações do BD
"""
def salvar(bd):
    print("Salvando alterações...")
    bd.salvar()
    print("Alterações salvas com sucesso!")
