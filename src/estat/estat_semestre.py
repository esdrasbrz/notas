"""
Classe responsável por realizar os cálculos matemáticos e estatísticos
para um semestre

Esdras R. Carmo
"""

from .estat_disciplina import *

class EstatSemestre:
    def __init__(self, bd, semestre):
        self.bd = bd
        self.semestre = semestre

        # disciplinas referentes à este semestre
        self.disciplinas = semestre.get_disciplinas(bd)
            
        # calcula as medias
        sum_notas_parcial = 0.0
        sum_pesos_parcial = 0

        sum_notas_total = 0.0
        sum_pesos_total = 0

        # percorre as disciplinas
        for disciplina in self.disciplinas:
            # instancia os calculos por disciplina
            estat = EstatDisciplina(self.bd, disciplina)
            
            sum_notas_total += disciplina.creditos * estat.media_total
            sum_pesos_total += disciplina.creditos

            # verifica se possui nota para adicionar ao parcial
            if estat.media_parcial:
                sum_notas_parcial += disciplina.creditos * estat.media_parcial
                sum_pesos_parcial += disciplina.creditos

        # medias calculadas
        self.media_total = sum_notas_total / sum_pesos_total if sum_pesos_total else 0.0
        self.media_parcial = sum_notas_parcial / sum_pesos_parcial if sum_pesos_parcial else 0.0

    """
    Função que imprime as médias totais e parciais de cada disciplina do semestre
    """
    def print_medias(self):
        # percorre as disciplinas
        for disciplina in self.disciplinas:
            # instancia os calculos por disciplina
            estat = EstatDisciplina(self.bd, disciplina)

            # imprime as estatísticas
            print("------- %s --------" % disciplina)
            print("Média Parcial: %.2lf" % estat.media_parcial)
            print("Média Total: %.2lf" % estat.media_total)
            print("Desvio Padrão: %.2lf" % estat.desvio_padrao)
            print()

