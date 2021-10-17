'''
o nome do arquivo 'modelo' foi escolhido
por que normalmente quando se cria um arquivo
em projetos de POO se da esse nome ao arquivo
que dara o conceito de classes que teram/daram
um dominio no nosso sistema.
'modelar uma classe é contruir ela, dar vida.'
'''
################ Classes #######################################
class Programa: #'Programa' de Programa de televisao =).
    def __init__(self, nome , ano , likes = 0):
        self._nome = nome
        self._ano = ano
        self._likes = likes
    #os get
    @property
    def nome(self):
        self._nome = str(self._nome).title()
        return self._nome
    @property
    def ano(self):
        return self._ano
    @property
    def likes(self):
        return int(self._likes)
    #os set
    @nome.setter
    def nome(self,novo_nome):
        self._nome = str(novo_nome).title()
    @ano.setter
    def ano(self,novo_ano):
        self._ano = novo_ano
    @likes.setter
    def likes(self,valor):
        self._likes = int(self._likes) + int(valor)

    #metodos da classe
    def dar_like(self):
        self._likes = self._likes + 1


class Filme(Programa):
    def __init__(self, nome , ano , duracao, likes=0):
        super().__init__(nome, ano , likes)
        self.__duracao = duracao
    @property
    def duracao(self):
        return self.__duracao
    @duracao.setter
    def duracao(self,nova_duracao):
        self.__duracao = nova_duracao

    #metodos da classe

class Serie(Programa):
    def __init__(self, nome, ano, temporadas, likes=0):
        super().__init__(nome , ano , likes)
        self.__temporadas = temporadas
    @property
    def temporadas(self):
        return self.__temporadas
    @temporadas.setter
    def temporadas(self,valor):
        self.__temporadas = valor

    #metodos da classe
    


############### MAIN ###########################################
if(__name__ == "__main__"):
    vingadores = Filme("vingadores: guerra infinita",2018,160)
    print("-"*30+"\n"+f'Filme: {vingadores.nome}\nAno: {vingadores.ano}\nDuraçao: {vingadores.duracao}\nLikes: {vingadores.likes}\n'+"-"*30)
    vingadores.dar_like()
    #atlanta = Serie("atlanta",2017,2,8)
    #print("-" * 30 + "\n" + f'Serie: {atlanta.nome}\nAno: {atlanta.ano}\nTemporadas: {atlanta.temporadas}\nLikes: {atlanta.likes}\n' + "-" * 30)


    print("-"*30+"\n"+f'Filme: {vingadores.nome}\nAno: {vingadores.ano}\nDuraçao: {vingadores.duracao}\nLikes: {vingadores.likes}\n'+"-"*30)
