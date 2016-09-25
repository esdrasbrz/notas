"""
Classe responsável por cada disciplina dependendo do semestre

Esdras R. Carmo
"""

class Disciplina:
    def __init__(self, nome='', creditos=0, semestre=None):
        self.nome = nome
        self.creditos = creditos

        # semestre ao qual pertence a disciplina
        self.semestre = semestre

    """
    Função que retorna uma lista de testes referentes à esta disciplina
    """
    def get_testes(self, bd):
        testes = []

        # percorre o bd
        for teste in bd.testes:
            if teste.disciplina == self:
                testes.append(teste)

        return testes
    
    def __str__(self):
        return "%s - %d créditos" % (self.nome, self.creditos)

    """
    Função para remover a disciplina e todos os seus testes
    """
    def remover(self, bd):
        testes = self.get_testes(bd)

        # percorre os testes removendo
        for teste in testes:
            teste.remover(bd)

        # procura a disciplina no bd
        for i, disciplina in enumerate(bd.disciplinas):
            if disciplina == self:
                break

        # remove a disciplina
        del bd.disciplinas[i]
