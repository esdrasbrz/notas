"""
Classe responsável por realizar os cálculos matemáticos/estatísticos
para determinada disciplina

Esdras R. Carmo
"""

import math

class EstatDisciplina:
    def __init__(self, bd, disciplina):
        self.disciplina = disciplina
        self.bd = bd
        
        # lista de testes referentes à disciplina
        self.testes = disciplina.get_testes(bd)
        
        # calcula as médias
        sum_notas_parcial = 0.0
        sum_pesos_parcial = 0

        sum_notas_total = 0.0
        sum_pesos_total = 0

        sum_desvio = 0.0
        qtd_notas = 0

        # percorre os testes
        for teste in self.testes:
            sum_notas_total += teste.peso * teste.nota if teste.nota != -1. else 0.
            sum_pesos_total += teste.peso

            # verifica a nota
            if teste.nota != -1.0:
                # adiciona nos somatórios parciais
                sum_notas_parcial += teste.peso * teste.nota
                sum_pesos_parcial += teste.peso

        # finaliza os cálculos de media
        self.media_parcial = sum_notas_parcial / sum_pesos_parcial if sum_pesos_parcial else 0.0
        self.media_total = sum_notas_total / sum_pesos_total if sum_pesos_total else 0.0

        # percorre para calcular o desvio padrão
        for teste in self.testes:
            if teste.nota != -1.0:
                sum_desvio += (teste.nota - self.media_parcial)**2
                qtd_notas += 1

        # finaliza o calculo de desvio
        self.desvio_padrao = math.sqrt(sum_desvio / (qtd_notas - 1)) if qtd_notas > 1 else 0.0

    """
    Função que imprime todos os testes e suas notas (se houver)
    """
    def print_notas(self):
        for teste in self.testes:
            print("Teste: %s | Peso: %d | Nota: %s" % (teste.nome, teste.peso, '%.2f' % teste.nota if teste.nota != -1.0 else 'SN'))

