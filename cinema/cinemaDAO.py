from DAO.ClienteDAO import ClienteDAO
from DAO.ComboDAO import ComboDAO
from DAO.FilmeDAO import FilmeDAO
from DAO.GeneroDAO import GeneroDAO
from DAO.IngressoDAO import IngressoDAO
from DAO.FilmeGeneroDAO import FilmeGeneroDAO
from DAO.SessãoDAO import SessaoDAO
from DAO.SalaDAO import SalaDAO
from DAO.AssentosDAO import AssentosDAO
from Cliente import Cliente
import sys
cliente = ClienteDAO()
lista_clientes = cliente.inicia()
filme = FilmeDAO()
lista_filmes = filme.inicia()
genero = GeneroDAO()
lista_generos = genero.inicia()
combo = ComboDAO()
lista_combos = combo.inicia()
ingresso = IngressoDAO()
lista_ingresso = ingresso.inicia()
sessao = SessaoDAO()
lista_sessoes = sessao.inicia()
relacao = FilmeGeneroDAO()
lista_relaçoes = relacao.inicia()

def login(nome, senha):
    for i in lista_clientes:
        if nome == i.nome and senha == i.senhas:
            print("login realizado!")
            usuario = Cliente(i.Id, i.nome, i.emails, i.senhas, i.sobrenomes, i.idades)
            return True
            break
    print("login ou senha incorretos, tente novamente")
    return False

h = login("deide", 123)
