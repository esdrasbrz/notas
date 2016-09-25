"""
Classe responsável por realizar os cálculos matemáticos/estatísticos
para determinada disciplina
"""

class EstatDisciplina:
    def __init__(self, bd, disciplina):
        self.disciplina = disciplina
        self.bd = bd
        
        # lista de testes referentes à disciplina
        self.testes = disciplina.get_testes(bd)

    """
    Função que imprime todos os testes e suas notas (se houver)
    """
    def print_notas(self):
        for teste in self.testes:
            print("Teste: %s | Peso: %d | Nota: %s" % (teste.nome, teste.peso, '%.2f' % teste.nota if teste.nota != -1.0 else 'SN'))

    """
    Função que calcula as médias parciais dos testes, i. e., apenas dos testes
    que já possuem nota cadastrada
    """
    def media_parcial(self):
        sum_notas = 0.0
        sum_pesos = 0

        # percorre os testes
        for teste in self.testes:
            # verifica a nota
            if teste.nota != -1.0:
                sum_notas += teste.peso * teste.nota
                sum_pesos += teste.peso

        return sum_notas / sum_pesos if sum_pesos else 0.0

    """
    Função que calcula a média total dos testes, sem se importar com os testes não feitos
    """
    def media_total(self):
        sum_notas = 0.0
        sum_pesos = 0

        # percorre os testes
        for teste in self.testes:
            sum_notas += teste.peso * teste.nota if teste.nota != -1.0 else 0.0
            sum_pesos += teste.peso

        return sum_notas / sum_pesos if sum_pesos else 0.0
