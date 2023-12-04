class Sala:
    def __init__(self, cod_sala, liberado):
        self.cod_sala = cod_sala
        self.liberado = liberado
    
    def getCodSala(self):
        return self.cod_sala
    def setCodSala(self, cod_sala):
        self.__cod_sala = cod_sala
    def getLiberado(self):
        return self.cod_sala
    def setLiberado(self, liberado):
        self.__liberado = liberado 
        