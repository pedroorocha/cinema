from conexão import conexao
from classes.Sessão import Sessão

class SessaoDAO:
    def __init__(self):
        None
    def inicia(self):
        c = conexao()
        sql = "SELECT * FROM Sessao"
        cursor = c.conn.execute(sql)
        sessoes = []
        for row in cursor.fetchall():
            sessao = Sessão(row[0], row[1], row[2])
            sessoes.append(sessao)
        return sessoes
    def inserir_sessao(self, capacidade, horario):
        c = conexao()
        sql = "INSERT INTO Sessao (Capacidade, Horario) VALUES (?,?)"
        cursor = c.conn.execute(sql, (capacidade, horario))
        c.conn.commit()
        c.conn.close()
        print("sessão inserida!")
    def deletar_sessao(self, ID):
        c = conexao()
        sql = "DELETE FROM Sessao WHERE Filme_Id = ?"
        cursor = c.conn.execute(sql, (ID,))
        c.conn.commit()
        c.conn.close()
        print("sessão deletada!")