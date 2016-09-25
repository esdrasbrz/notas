"""
Classe responsável por determinar um semestre caracterizado pelo ano e período (primeiro
ou segundo)

Esdras R. Carmo
"""

from datetime import datetime

class Semestre:
    def __init__(self, ano=datetime.now().year, periodo=1):
        self.ano = ano
        self.periodo = periodo

    """
    Função que retorna uma lista de disciplinas cadastradas para este semestre
    """
    def get_disciplinas(self, bd):
        disciplinas = []

        # percorre o bd
        for disciplina in bd.disciplinas:
            if disciplina.semestre == self:
                disciplinas.append(disciplina)

        return disciplinas
    
    def __str__(self):
        return "%d - período %d" % (self.ano, self.periodo)

    """
    Função de remoção para remover todas as disciplinas
    """
    def remover(self, bd):
        disciplinas = self.get_disciplinas(bd)

        # percorre as disciplinas removendo
        for disciplina in disciplinas:
            disciplina.remover(bd)

        # procura o semestre no bd
        for i, semestre in enumerate(bd.semestres):
            if semestre == self:
                break

        # remove o semestre
        del bd.semestres[i]
