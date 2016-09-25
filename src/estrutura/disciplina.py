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

        # lista de testes que irá avaliar aquela disciplina
        self.testes = []

    def __str__(self):
        return "%s - %d créditos" % (self.nome, self.creditos)
