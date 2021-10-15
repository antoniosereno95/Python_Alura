
class Conta:

    def __init__(self,numero,titular,saldo,limite=1000):
        #1.self refencia o endereço de memoria onde o bjeto foi armazenado
        '''
        2.'limite=1000' ali encima no construtor seta o limite sempre com aquele valor,
        e se necessario o valor pode ser alterado na inicializaçao do objeto, oq vai utilizar
        a variavel 'limite' que foi criada ali embaixo e substituirar
        o valor padrao de limite pelo valor digitado. '''
        #3. (...)
        print("Construindo o Objeto que esta no endereço {}.".format(self))
        self.numero_da_conta = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print("O saldo de {} pertence ao titular {} da conta {}".format(self.saldo,self.titular,self.numero_da_conta))

    def deposita(self,valor):
        self.saldo += valor

    def saca(self,valor):
        self.saldo -= valor



if(__name__ == "__main__"):
    from conta import Conta
    ''' Esse from é otimo, oq esta aocntecendo aqui nesse momento é:
    eu estou dizendo de qual arquivo o python deve tirar determinada 
    importaçao. 'do arquivo conta, importe a class Conta'(nao confundir os nomes)
    '''
    
    conta = Conta(123,"antonio",6000,25000)
    conta.extrato()



