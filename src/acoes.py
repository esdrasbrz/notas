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

# Exibe todos os objetos para o usuário selecionar
def _list_objetos(objs):
    for i, obj in enumerate(objs):
        print("%d: %s" % (i, obj))

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
        _list_objetos(bd.semestres)

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
        _list_objetos(bd.semestres)
        print()
        i_sem = int(input("Digite o índice do semestre: "))

        # cache na lista de disciplinas
        disciplinas = bd.semestres[i_sem].get_disciplinas(bd)
        
        # escolhe a disciplina
        print("Selecione a disciplina")
        _list_objetos(disciplinas)
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
Função para setar uma nova nota
"""
def set_nota(bd):
    try:
        print("Selecione o semestre")
        _list_objetos(bd.semestres)
        print()
        i_sem = int(input("Digite o índice do semestre: "))

        # cache da lista de disciplinas
        disciplinas = bd.semestres[i_sem].get_disciplinas(bd)

        # escolhe a disciplina
        print("Selecione a disciplina")
        _list_objetos(disciplinas)
        print()
        i_disc = int(input("Digite o índice da disciplina: "))

        # cache da lista de testes
        testes = bd.disciplinas[i_disc].get_testes(bd)

        # escolhe o teste
        print("Seleciona o teste")
        _list_objetos(testes)
        print()
        i_teste = int(input("Digite o índice do teste: "))

        nota = float(input("Digite sua nota (separe decimais com '.'): "))

        # atualiza o teste
        testes[i_teste].nota = nota

        print("Nota inserida com sucesso!")
        if nota > 9:
            print("... e que nota em!? =D")
    except:
        print("Desculpe, algum erro ocorreu :(")

"""
Função para salvar todas as alterações do BD
"""
def salvar(bd):
    print("Salvando alterações...")
    bd.salvar()
    print("Alterações salvas com sucesso!")
