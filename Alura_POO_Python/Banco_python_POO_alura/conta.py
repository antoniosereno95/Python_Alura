
class Conta:
    #construtor
    def __init__(self,numero,titular,saldo,limite=1000):
        #1.self refencia o endereço de memoria onde o bjeto foi armazenado
        '''
        2.'limite=1000' ali encima no construtor seta o limite sempre com aquele valor,
        e se necessario o valor pode ser alterado na inicializaçao do objeto, oq vai utilizar
        a variavel 'limite' que foi criada ali embaixo e substituirar
        o valor padrao de limite pelo valor digitado. '''
        #3. (...)
        print("Construindo o Objeto que esta no endereço {}.".format(self))
        self.__numero_da_conta = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
    #os get
    def getNumero_da_conta(self):
        return self.__numero_da_conta
    def getTitular(self):
        return self.__titular
    def getSaldo(self):
        return self.__saldo
    def getLimite(self):
        return self.__limite
    #os set
    def setNumero_da_conta(self,valor):
        self.__numero_da_conta = valor
    def setTitular(self,valor):
        self.__titular = valor
    def setSaldo(self,valor):
        self.__saldo = valor
    def setLimite(self,valor):
        self.__limite = valor

    #os metodos
    def extrato(self):
        print("O saldo de {} pertence ao titular {} da conta {}".format(self.getSaldo(),self.getTitular(),self.getNumero_da_conta()))

    def depositar(self,valor):
        self.setSaldo(self.getSaldo()+valor)

    def sacar(self,valor):
        self.setSaldo(self.getSaldo()-valor)

    def transferir(self,conta1,conta2):
        valor = input("Digite o valor a ser tranferido: ")
        while(not valor.isnumeric()):
            valor = input("Digite um valor(numerico) aceitavel: ")
        valor = int(valor)
        if(valor <= conta1.getSaldo()):
            try:
                conta1.sacar(valor)
                conta2.depositar(valor)
            except: print(">>>Erro, na transferencia.")
            else: print(">Tranferencia realizada com sucesso<")
        else:
            print(">>>Erro!Saldo insuficiente.")


#################  Main  ##########################################
if(__name__ == "__main__"):
    from conta import Conta
    ''' Esse from é otimo, oq esta aocntecendo aqui nesse momento é:
    eu estou dizendo de qual arquivo o python deve tirar determinada 
    importaçao. 'do arquivo conta, importe a class Conta'(nao confundir os nomes)
    '''

    conta = Conta(123,"geraldo",6000,25000)
    conta.extrato()
    conta2 = Conta(124,"juvenal",6000)
    conta2.extrato()

    conta.transferir(conta,conta2)

    conta.extrato()
    conta2.extrato()




