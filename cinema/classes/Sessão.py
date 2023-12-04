
class Sessão:
    def __init__(self, sessao_Id, capacidade, horario):
        self.sessao_Id = sessao_Id
        self.capacidade = capacidade
        self.horario = horario

    def getsessao_Id(self):
        return self.__sessao_Id
    def setsessao_Id(self, sessao_Id):
        self.__sessao_Id = sessao_Id
    def getCapacidade(self):
        return self.__capacidade
    def setCapacidade(self, capacidade):
        self.__capacidade = capacidade