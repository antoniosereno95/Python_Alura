

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
    @property
    def numero_da_conta(self):
        return self.__numero_da_conta
    @property
    def titular(self):
        return self.__titular
    @property
    def saldo(self):
        return self.__saldo
    @property
    def limite(self):
        return self.__limite
    #os set
    @numero_da_conta.setter
    def numero_da_conta(self,valor):
        self.__numero_da_conta = valor
    @titular.setter
    def titular(self,valor):
        self.__titular = valor
    @saldo.setter
    def saldo(self,valor):
        self.__saldo = valor
    @limite.setter
    def limite(self,valor):
        self.__limite = valor

    #os metodos
    def extrato(self):
        print("O saldo de {} pertence ao titular {} da conta {}".format(self.saldo,self.titular,self.numero_da_conta))

    def depositar(self,valor):
        self.saldo = self.saldo + valor

    def sacar(self,valor):
        if(self.__pode_sacar(valor)):
            self.saldo = self.saldo - valor
        else:
            print(">>>Erro!Saldo insuficiente.")
    
    #este metodo 'pode_sacar()' foi declarado um METODO PRIVADO da class conta pois ele so deve ser usado dentro da classe
    def __pode_sacar(self, valor_a_sacar):
        return valor_a_sacar <= (self.limite + self.saldo)

    def transferir(self,conta1,conta2):
        valor = input("Digite o valor a ser tranferido: ")
        while(not valor.isnumeric()):
            valor = input("Digite um valor(numerico) aceitavel: ")
        valor = int(valor)
        if(valor <= conta1.saldo):
            try:
                conta1.sacar(valor)
                conta2.depositar(valor)
            except: print(">>>Erro, na transferencia.")
            else: print(">Tranferencia realizada com sucesso<")
        else:
            print(">>>Erro!Saldo insuficiente.")
    '''
    def cliente_inadimplencia(self):
        if(self.saldo <= self.limite+self.saldo):
            Cliente.inadimplente = True
        else:
            Cliente.inadimplente = False
    '''

#################  Main  ##########################################
if(__name__ == "__main__"):
    from cliente import Cliente
    from conta import Conta
    ''' Esse from é otimo, oq esta aocntecendo aqui nesse momento é:
    eu estou dizendo de qual arquivo o python deve tirar determinada 
    importaçao. 'do arquivo conta, importe a class Conta'(nao confundir os nomes)
    '''

    conta1 = Conta(123, "geraldo", 10, 10)
    conta1.extrato()
    conta2 = Conta(124,"juvenal",6000)
    conta2.extrato()
    '''#teste pra ver se uma conta poderia armazenar valores negativos#
    conta1.sacar(20)
    conta1.extrato()
    '''
    #essa tranferencia deve dar errado, se eu for tranferir mais que 21 reais
    conta1.transferir(conta1, conta2)

    conta1.extrato()
    print("conta1==>{}".format(Cliente.inadimplente))
    conta2.extrato()

    #essa tranferencia deve funcionar independente do valor
    conta2.transferir(conta2, conta1)
    conta1.extrato()
    conta2.extrato()

    #essa transferencia deve funcionar se na ultima tranferencia eu tiver transferido um valor maior que o limite da conta1
    conta1.transferir(conta1, conta2)

    conta1.extrato()
    conta2.extrato()

