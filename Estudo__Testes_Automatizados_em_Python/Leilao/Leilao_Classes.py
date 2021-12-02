############### Imports ###########################
import sys
"""
Esse pacote 'sys' traz com le informaçoes do sistema,
e no caso dessa implementaçao eu vou extrair dele os 
(maiores e menores) valores possiveis de um float, tipo o 
'MAX_VALEU' e 'MIN_VALEU' no java.
"""
############### Classes ###########################
class Usuario:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome


class Lance:

    def __init__(self,usuario:Usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.lista_de_lances = []

    @property
    def lances(self):
        return self.lista_de_lances

class Avaliador:

    def __init__(self):
        self.maior_lance = sys.float_info.min #--> float MaiorLance = Float.MIN_VALEU ...(esse codigo corresponde a isso no java).
        self.menor_lance = sys.float_info.max #--> float MenorLance = Float.MAX_VALEU ...(esse codigo corresponde a isso no java).

    def Avalia(self, leilao:Leilao):
        for lance in leilao.lista_de_lances: #esse 'lance' aqui é sao as classes Lance que estao da lista_de_lances, que por sua vez é uma propriedade da classe Leilao.
            if(lance.valor > self.maior_lance):
                self.maior_lance = lance.valor
            elif(lance.valor < self.menor_lance):
                self.menor_lance = lance.valor







