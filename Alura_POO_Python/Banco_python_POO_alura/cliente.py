from conta import Conta

class Cliente:
    #construtor
    def __init__(self, nome , inadimplente = False):
        self.__nome = nome
        #verifica se i atributo inadimplente é do tipo bool
        try:
            inadimplente = bool(inadimplente)
        except:print(">>>Erro! variavel inadinplemte deve ser do tipo bool")
        else:self.__inadimplente = inadimplente


    '''essa sintaxe de '@property' e de '@atributo.setter' 
    so serve para deixar a chamada dessas funçoes mais amigavel, 
    apesar dos getters and setters ja serem amigaveis o suficiente 
    para o meu gosto(acostumado com meu javinha ehuehuehe)'''

    @property
    def nome(self):
        return self.__nome.title()
        # noinspection PyUnreachableCode
        '''
        quando eu uso essa propriedade '@property' 
        eu to dizendo que o (metodo->)'def nome',que era omeu antigo getter,
        vai servir como uma funçao de propriedade para a vaiavel privada '__nome', 
        que nesse caso, alem de retornar o seu valor(como uma getter), 
        ela tambem bota ela com a primeira letra maiuscula(funçao 'title()').'''

    @nome.setter
    def nome(self, valor):
        self.__nome = valor
        '''
        Esse metodo 'def nome(valor)' foi declarado com o
        @nome.setter. ele faz com que o metodo seja reconhecido 
        como um setter, mas esse metodo setter esta refenciado ao 
        outro medoto 'def nome' que é um @property, pois quando
        ha um @property no jogo, o unico meio de acessar o atributo
        '__nome' é por ele, **É basicamnete um encapsulamento de 
        atributo(o @property)** e o @nome.setter serve como o setter
        desse encapsulamento de atributo.'''

    @property
    def inadimplente(self):
        return self.__inadimplente
    @inadimplente.setter
    def inadimplente(self,boolean):
        self.__inadimplente = boolean



if(__name__ == "__main__"):
    from cliente import Cliente
    cliente1 = Cliente("kiko")
    print(cliente1.nome)

    cliente1.nome = "sergio"
    print(cliente1.nome)

