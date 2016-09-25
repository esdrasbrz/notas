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

        # lista com todas as disciplinas cadastradas naquele semestre
        self.disciplinas = []

    def __str__(self):
        return "%d - período %d" % (self.ano, self.periodo)
