"""
Classe responsável por mapear cada teste que irá avaliar uma disciplina

Esdras R. Carmo
"""

class Testes:
    def __init__(self, nome='', peso=1, nota=-1.0, disciplina=None):
        self.nome = nome
        self.peso = peso
        self.nota = nota # inicia com nota -1, significando que o usuário não fez o teste ainda

        self.disciplina = disciplina # disciplina a qual se relaciona o teste


    def __str__(self):
        teste = '%s - Peso: %d' % (self.nome, self.peso)
        if self.nota != -1.0:
            teste += ' - Nota: %.2f' % self.nota

        return teste
