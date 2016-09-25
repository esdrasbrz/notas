"""
Arquivo com as ações de seleção de cada item do menu principal

Esdras R. Carmo
"""

from estrutura import *
from estat import *

# Função para salvar todas as alterações do BD
def salvar(bd):
    print("Salvando alterações...")
    bd.salvar()
    print("Alterações salvas com sucesso!")

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

# Função para selecionar o semestre com base no usuário
def _sel_semestre(bd):
    print("Selecione o semestre")
    _list_objetos(bd.semestres)
    print()
    i = int(input("Digite o índice do semestre: "))

    return bd.semestres[i]

# Função para selecionar a disciplina com base no usuário
def _sel_disciplina(bd):
    semestre = _sel_semestre(bd)

    # cache das disciplinas
    disciplinas = semestre.get_disciplinas(bd)

    print("Selecione a disciplina")
    _list_objetos(disciplinas)
    print()
    i = int(input("Digite o índice da disciplina: "))

    return disciplinas[i]

# Função para selecionar o teste com base no usuário
def _sel_teste(bd):
    disciplina = _sel_disciplina(bd)

    # cache dos testes
    testes = disciplina.get_testes(bd)

    print("Selecione o teste")
    _list_objetos(testes)
    print()
    i = int(input("Digite o índice do teste: "))

    return testes[i]

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
        semestre = _sel_semestre(bd)
        nome = input("Digite o nome da disciplina: ")
        creditos = int(input("Digite quantos créditos ela possui: "))

        disciplina = Disciplina(nome=nome, creditos=creditos, semestre=semestre)
        bd.disciplinas.append(disciplina)

        print("Disciplina inserida com sucesso!")
    except:
        print("Desculpe, algum erro ocorreu :(")

# Função para inserir um novo teste
def new_teste(bd):
    try:
        # recebe a disciplina
        disciplina = _sel_disciplina(bd)

        # loop para cadastrar vários testes
        while True:
            print()
            nome = input("Digite o nome do teste: ")
            peso = int(input("Qual o peso? "))
            
            # instancia e insere no bd
            teste = Testes(nome=nome, peso=peso, disciplina=disciplina)
            bd.testes.append(teste)

            opcao = input("Deseja cadastrar mais um teste? (S/n) ")
            if opcao and opcao.upper() == 'N':
                break
    except:
        print("Desculpe, algum erro ocorreu :(")

# Função para remover um semestre
def del_semestre(bd):
    try:
        # recebe o semestre
        semestre = _sel_semestre(bd)

        resp = input("Tem certeza que deseja excluir o semestre (e tudo que depende dele)? (s/N) ")

        if resp and resp.upper() == 'S':
            semestre.remover(bd)

            print("Semestre removido com sucesso!")
    except:
        print("Desculpe, algum erro ocorreu :(")

# Função para remover uma disciplina
def del_disciplina(bd):
    try:
        # recebe a disciplina
        disciplina = _sel_disciplina(bd)

        resp = input("Tem certeza que deseja excluir a disciplina (e tudo que depende dela)? (s/N) ")

        if resp and resp.upper() == 'S':
            disciplina.remover(bd)

            print("Disciplina removido com sucesso!")
    except:
        print("Desculpe, algum erro ocorreu :(")

# Função para remover um semestre
def del_teste(bd):
    try:
        # recebe o teste
        teste = _sel_teste(bd)

        resp = input("Tem certeza que deseja excluir o teste? (s/N) ")

        if resp and resp.upper() == 'S':
            teste.remover(bd)

            print("Teste removido com sucesso!")
    except:
        print("Desculpe, algum erro ocorreu :(")

# Função para setar uma nova nota
def set_nota(bd):
    try:
        teste = _sel_teste(bd)
        nota = float(input("Digite sua nota (separe decimais com '.'): "))

        # atualiza o teste
        teste.nota = nota

        print("Nota inserida com sucesso!")
        if nota > 9:
            print("... e que nota em!? =D")
    except:
        print("Desculpe, algum erro ocorreu :(")

# Função que imprime as estatísticas por disciplina
def estat_disciplina(bd):
    try:
        # escolhe a disciplina
        disciplina = _sel_disciplina(bd)

        # instancia a classe responsável pelos calculos
        estat = EstatDisciplina(bd, disciplina)

        # imprime a tabela com todas as notas
        print()
        estat.print_notas()
        print()

        # imprime as estatísticas
        print("Média parcial: %.2f" % estat.media_parcial)
        print("Média total: %.2f" % estat.media_total)
        print("Desvio padrão: %.2f" % estat.desvio_padrao)
    except:
        print("Desculpe, algum erro ocorreu :(")

# Função que imprime estatística por semestre
def estat_semestre(bd):
    try:
        # escolhe o semestre
        semestre = _sel_semestre(bd)

        # instancia da classe responsável pelos cálculos
        estat = EstatSemestre(bd, semestre)

        # imprime a tabela com as médias
        print()
        estat.print_medias()
        print()

        print("------- Estatísticas do semestre --------")
        print("Média parcial: %.2f" % estat.media_parcial)
        print("Média total: %.2f" % estat.media_total)
    except:
        print("Desculpe, algum erro ocorreu :(")
