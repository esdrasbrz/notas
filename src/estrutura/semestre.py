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
