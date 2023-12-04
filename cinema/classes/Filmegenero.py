class filmeGenero():
    def __init__(self, Idfilme, Idgenero):
        self.Idfilme = Idfilme
        self.Idgenero = Idgenero
        
    def  getIdfilme(self):
        return self.__Idfilme
    def setIdfilme(self, Idfilme):
        self.__Idfilme = Idfilme
    def getIdgenero(self):
        return self.__Idgenero
    def setIdgenero(self, Idgenero):
        self.__Idgenero = Idgenero