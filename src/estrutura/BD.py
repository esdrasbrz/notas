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

    """
    Função para salvar todas as alterações nos arquivos
    """
    def salvar(self):
        # cria as strings contendo os dados que irão para o arquivo
        str_sem = ''
        str_disc = ''
        str_testes = ''

        # percorre os semestres inserindo
        for semestre in self.semestres:
            str_sem += "%d;%d\n" % (semestre.ano, semestre.periodo)

        # percorre as disciplinas inserindo
        for disciplina in self.disciplinas:
            str_disc += "%s;%d;" % (disciplina.nome, disciplina.creditos)

            # procura o indice do semestre
            i = 0
            for semestre in self.semestres:
                if semestre == disciplina.semestre:
                    break
                i += 1

            str_disc += "%d\n" % i

        # percorre os testes inserindo
        for teste in self.testes:
            str_testes += "%s;%d;%.2f;" % (teste.nome, teste.peso, teste.nota)

            # procura o índice da disciplina
            i = 0
            for disciplina in self.disciplinas:
                if disciplina == teste.disciplina:
                    break
                i += 1

            str_testes += "%d\n" % i


        # abre os arquivos para gravar
        with open('../dados/semestres', 'w') as file_sem:
            file_sem.write(str_sem)
        with open('../dados/disciplinas', 'w') as file_disc:
            file_disc.write(str_disc)
        with open('../dados/testes', 'w') as file_testes:
            file_testes.write(str_testes)
