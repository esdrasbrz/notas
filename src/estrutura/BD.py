"""
Classe responsável por armazenar e manipular toda a base de dados
"""

from .semestre import *
from .disciplina import *
from .testes import *

class BD:
    def __init__(self):
        self.semestres = []
        self.disciplinas = []
        self.testes = []
    
    """
    Função para abrir os arquivos da base de dados
    """
    def abrir(self):
        try:
            # abre os arquivos da base
            # TODO usar path absolutos
            arq_sem = open('../dados/semestres')
            arq_disc = open('../dados/disciplinas')
            arq_testes = open('../dados/testes')
            
            # le todos os dados dos arquivos
            sem = arq_sem.read().split('\n')
            disc = arq_disc.read().split('\n')
            testes = arq_testes.read().split('\n')

            # percorre lendo os semestres
            for dados in sem:
                if not dados:
                    continue

                # separa os dados daquele semestre
                dados = dados.split(';')
                
                # instancia o novo semestre e armazena na lista
                semestre = Semestre(int(dados[0]), int(dados[1]))
                self.semestres.append(semestre)

            # percorre lendo as disciplinas
            for dados in disc:
                if not dados:
                    continue
                
                # separa os dados
                dados = dados.split(';')

                # instancia e armazena na lista
                disciplina = Disciplina(dados[0], int(dados[1]), self.semestres[int(dados[2])])
                self.disciplinas.append(disciplina)

            # percorre lendo os testes
            for dados in testes:
                if not dados:
                    continue

                # separa os dados
                dados = dados.split(';')

                # instancia e armazena na lista
                teste = Testes(dados[0], int(dados[1]), float(dados[2]), self.disciplinas[int(dados[3])])
                self.testes.append(teste)

            arq_sem.close()
            arq_disc.close()
            arq_testes.close()
            print("Base de dados lida com sucesso!")
        except FileNotFoundError:   
            print("Base de dados não encontrada...") # silencia o caso de não existir base de dados ainda

