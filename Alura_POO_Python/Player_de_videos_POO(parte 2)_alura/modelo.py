'''
o nome do arquivo 'modelo' foi escolhido
por que normalmente quando se cria um arquivo
em projetos de POO se da esse nome ao arquivo
que dara o conceito de classes que teram/daram
um dominio no nosso sistema.
'modelar uma classe é contruir ela, dar vida.'
'''
################ Classes #######################################

class Filmes:
    def __init__(self, nome , ano , duracao):
        self.__nome = nome
        self.__ano = ano
        self.__duracao = duracao

    #os get
    @property
    def nome(self):
        return self.__nome
    @property
    def ano(self):
        return self.__ano
    @property
    def duracao(self):
        return self.__duracao

    #os set
    @nome.setter
    def nome(self,novo_nome):
        self.__nome = novo_nome
    @ano.setter
    def ano(self,novo_ano):
        self.__ano = novo_ano
    @duracao.setter
    def duracao(self,nova_duracao):
        self.__duracao = nova_duracao

    #metodos da classe


class Serie:
    def __init__(self, nome , ano , temporadas):
        self.__nome = nome
        self.__ano = ano
        self.__temporadas = temporadas


############### MAIN ###########################################
if(__name__ == "__main__"):
    pass