####### Classes ###################
class Carro:
    def __init__(self,nome,marca,ano,numero_portas ,consumo_litros,kilometragem,lotaçao):
        self.__nome = nome
        self.__marca = marca
        self.__ano = ano
        self.__numero_portas = numero_portas
        self.__consumo_litros = consumo_litros
        self.__kilometragem = kilometragem
        self.__lotacao = lotaçao

    @property
    def nome(self):
        return self.__nome
    @property
    def marca(self):
        return self.__marca
    @property
    def ano(self):
        return self.__ano
    @property
    def lotaçao(self):
        return self.__lotacao
    @property
    def numero_portas(self):
        return self.__numero_portas
    @property
    def kilometragem(self):
        return self.__kilometragem
    @property
    def consumo_litros(self):
        return self.__consumo_litros
    @kilometragem.setter
    def kilometragem(self,valor):
        self.kilometragem = self.kilometragem + int(valor)
    @consumo_litros.setter
    def consumo_litros(self,novo_consumo):
        self.consumo_litros = novo_consumo

    #metodos da classe
    def __str__(self):
        return f'Marca:{self.marca};Nome:{self.nome};Ano:{self.ano};Portas:{self.numero_portas};Consumo medio:{self.consumo_litros};Kilometragem:{self.kilometragem};Lotação:{self.lotaçao};'

    def altera_kilometragem(self,nova_kilometragem):
        pass

    def altera_consumo(self):
        pass
        #colocar mais um litro por kilometro a cada 10.000 kilometros rodados

class Carro_Esportivo(Carro):
    def __init__(self,nome,marca,ano,numero_portas,consumo_litros,kilometragem,lotaçao,velocidade_maxima):
        super().__init__(nome,marca,ano,numero_portas,consumo_litros,kilometragem,lotaçao)
        self.__velocidade_maxima = velocidade_maxima
        # try:
        #     if(numero_portas > 2):
        #         print("Numero de portas incoerente,deseja modificar?(s/n)")
        #         r = input()
        #         if(str(r).upper() == "S"):
        #             n = input("digite: ")
        #             numero_portas = n
        # except:print("Carros Esportivos tem 2 ou menos portas.")
        # self.__numero_portas = numero_portas

    @property
    def velocidade_maxima(self):
        return self.__velocidade_maxima

    def __str__(self):
        return f'Marca:{self.marca};Nome:{self.nome};Ano:{self.ano};Velocidade Maxima:{self.velocidade_maxima};Portas:{self.numero_portas};Consumo medio:{self.consumo_litros}Km/L;Kilometragem:{self.kilometragem};Lotação:{self.lotaçao};'

class Carro_Familiar(Carro):
    def __init__(self,nome,marca,ano,numero_portas ,consumo_litros,kilometragem,lotaçao,van=False):
        super().__init__(nome,marca,ano,numero_portas ,consumo_litros,kilometragem,lotaçao)
        self.__van = van
    #se for van=true ou tiver mais de 5 de lotaçao é carro familiar

    @property
    def van(self):
        if(self.__van == True):
            r = f'Sim'
        else:
            r = f'Não'
        return r

    def __str__(self):
        return f'Marca:{self.marca};Nome:{self.nome};Ano:{self.ano};Portas:{self.numero_portas};Consumo medio:{self.consumo_litros}Km/L;Kilometragem:{self.kilometragem};Lotação:{self.lotaçao};Estilo van:{self.van};'

class Carro_Popular(Carro):
    def __init__(self,nome, marca, ano, numero_portas, consumo_litros, kilometragem, lotaçao):
        super().__init__(nome, marca, ano, numero_portas, consumo_litros, kilometragem, lotaçao)
    #todo carro popular tem lotaçao igual a 5

class Moto:
    def __init__(self,nome, marca,ano, cilindragem, consumo):
        self.__ano = ano
        self.__nome = nome
        self.__marca = marca
        self.__cilindragem = cilindragem
        self.__consumo = consumo

    @property
    def nome(self):
        return self.__nome
    @property
    def ano(self):
        return self.__ano
    @property
    def marca(self):
        return self.__marca
    @property
    def cilindragem(self):
        return self.__cilindragem
    @property
    def consumo(self):
        return self.__consumo

    def __str__(self):
        return f'Marca:{self.marca};Nome:{self.nome};Ano:{self.ano};Cilindradas:{self.cilindragem};Consumo medio:{self.consumo} Km/L;'

class Moto_esportiva(Moto):
    def __init__(self,nome, marca,ano, cilindragem, consumo, velocidade_maxima):
        super().__init__(nome, marca,ano, cilindragem, consumo)
        self.__velocidade_maxima = velocidade_maxima

    @property
    def velocidade_maxima(self):
        return self.__velocidade_maxima

    def __str__(self):
        return f'Marca:{self.marca};Nome:{self.nome};Ano:{self.ano};Cilindradas:{self.cilindragem};Velocidade Maxima:{self.velocidade_maxima};Consumo medio:{self.consumo} Km/L;'

class Moto_popular(Moto):
    def __init__(self, nome, marca, ano, cilindragem, consumo):
        super().__init__(nome, marca, ano, cilindragem, consumo)

class Barco():
    def __init__(self, nome, modo_de_locomocao, ocupacao):
        self.__nome = nome
        self.__modo_de_locomocao = modo_de_locomocao
        self.__ocupacao = ocupacao

    @property
    def nome(self):
        return self.__nome
    @property
    def locomoçao(self):
        return self.__modo_de_locomocao
    @property
    def ocupacao(self):
        return self.__ocupacao

    def __str__(self):
        return f'Nome da embarcação:{self.nome};Modo de Locomoção:{self.locomoçao};Ocupação Maxima:{self.ocupacao};'

class Bote(Barco):
    def __init__(self, nome, modo_de_locomocao, ocupacao, remos):
        super().__init__(nome, modo_de_locomocao, ocupacao)
        self.__remos = remos

    @property
    def remos(self):
        return self.__remos

    def __str__(self):
        return f'Nome da embarcação:{self.nome};Modo de Locomoção:{self.locomoçao};Remos inclusos:{self.remos};Ocupação Maxima:{self.ocupacao};'

class Lancha(Barco):
    def __init__(self, nome, modo_de_locomocao, ocupacao):
        super().__init__(nome, modo_de_locomocao, ocupacao)

class Yate(Barco):
    def __init__(self, nome, modo_de_locomocao, ocupacao):
        super().__init__(nome, modo_de_locomocao, ocupacao)

class Pessoa():
    def __init__(self,nome,sexo,idade,cpf,endereco):
        self.__nome = nome
        self.__idade = idade
        self.__sexo = sexo
        self.__cpf = cpf
        self.__endereco = endereco

    @property
    def nome(self):
        return self.__nome
    @property
    def idade(self):
        return self.__idade
    @property
    def sexo(self):
        return self.__sexo
    @property
    def cpf(self):
        return self.__cpf
    @property
    def endereço(self):
        return self.__endereco
    @endereço.setter
    def endereço(self,novo_endereço):
        self.__endereco = novo_endereço

class Cliente(Pessoa):
    def __init__(self,nome,sexo,idade,cpf,endereco,metodo_de_pagamento):
        super().__init__(nome,sexo,idade,cpf,endereco)
        self.__metodo_de_pagamento = metodo_de_pagamento

    @property
    def metodo_de_pagamento(self):
        return self.__metodo_de_pagamento
    @metodo_de_pagamento.setter
    def metodo_de_pagamento(self,novo):
        self.__metodo_de_pagamento = novo

    def __str__(self):
        return f'Nome do Cliente:{self.nome};Sexo:{self.sexo};Idade:{self.idade};Cpf:{self.cpf};Endereço:{self.endereço};Metodo de Pagamento:{self.metodo_de_pagamento}'

class Funcionario(Pessoa):
    #todos os funcionarios aqui serao caixas, mas é um aboa ideia depois oclocar um gerente tambem.
    def __init__(self,nome,sexo,idade,cpf,endereco):
        super().__init__(nome,sexo,idade,cpf,endereco)

    def __str__(self):
        return f'Nome do funcionario:{self.nome};Sexo:{self.sexo};Idade:{self.idade};Cpf:{self.cpf};Endereço:{self.endereço}'

######## Metodos #####################
def Existe_arquivo(nome):
    try:
        a = open(nome,'r')
        a.close()
    except:
        FileNotFoundError
        return False
    else:
        #print(">arquivo carregado com sucesso<")
        return True

#abre arquivo
#add no arquivo
#carega informaçoes dos arquivos

def Menu_devoluçao():
    print("*" * 42)
    print("     -Menu de Devolução-   ")
    print("1.Devolver Carro")
    print("2.Devolver Moto")
    print("3.Devolver Barco")
    print("4.Voltar")
    #print("*" * 42)

def Menu_aluguel():
    print("*" * 42)
    print("     -Menu de Aluguel-   ")
    print("1.Alugar Carro")
    print("2.Alugar Moto")
    print("3.Alugar Barco")
    print("4.Voltar")
    #print("*" * 42)

def Menu_Principal():
    print("*" * 42)
    print("     -Menu de Principal-   ")
    print("1.Alugar.")
    print("2.Devolver.")
    print("3.Analizar Banco de Dados.")
    print("4.Sair")
    print("*" * 42)

def Cria_listas_de_objetos_CARROS():
    Lista_de_obj_carros_esportivos = []
    Lista_de_obj_carros_familiares = []
    Lista_de_obj_carros_populares = []

    if(Existe_arquivo("Locadora_Carros.txt")):
        with open("Locadora_Carros.txt","r") as arquivo:
            for linha_do_arquivo in arquivo:
                linhas = linha_do_arquivo.split("\n")
                '''linhas é uma lista e retorna esse conteudo aqui:
                --> ['AMG;merecedes-benz;2020;2;14;0;2;320;False\\n', '']
                #print(linhas)
                '''
                palavras = linhas[0].split(";")
                palavras[8] = palavras[8].removesuffix("\\n")#tratamento da ultima string que vem com esse bagulho feioso ai no final dela.
                #print(palavras)

                if(int(palavras[6])>5 or palavras[8]=="True"):
                    carro_familiar = Carro_Familiar(str(palavras[0]),str(palavras[1]),int(palavras[2]),int(palavras[3]),float(palavras[4]),int(palavras[5]),int(palavras[6]),bool(palavras[8]))
                    Lista_de_obj_carros_familiares.append(carro_familiar)
                if(int(palavras[7])!=0):
                    carro_esportivo = Carro_Esportivo(str(palavras[0]),str(palavras[1]),int(palavras[2]),int(palavras[3]),float(palavras[4]),int(palavras[5]),int(palavras[6]),int(palavras[7]))
                    Lista_de_obj_carros_esportivos.append(carro_esportivo)
                if(int(palavras[6])==5 and int(palavras[7])==0):
                    carro_popular = Carro_Popular(str(palavras[0]),str(palavras[1]),int(palavras[2]),int(palavras[3]),float(palavras[4]),int(palavras[5]),int(palavras[6]))
                    Lista_de_obj_carros_populares.append(carro_popular)

    return Lista_de_obj_carros_populares,Lista_de_obj_carros_familiares,Lista_de_obj_carros_esportivos

def Listagem_dos_Carros_Dinponiveis():
    print("Carros Esportivos:")
    k = 1
    for c in Lista_de_obj_carros_esportivos:
        print(f"{k}:")
        print(c)
        k+=1

    print("Carros Familiares:")
    k = 1
    for c in Lista_de_obj_carros_familiares:
        print(f"{k}:")
        print(c)
        k += 1
    print("Carros Pupolares:")
    k = 1
    for c in Lista_de_obj_carros_populares:
        print(f"{k}:")
        print(c)
        k += 1

########## Metodos obsoletos ##############
def Valida_cpf_cliente_por_arquivo(cpf_cliente):
    # essa validaçao de cpf por arquivo ficou obsoleta deposi deu começar a utilizar as listas de objetos,vou deixar so por deixar mesmo.
    encontrei = False
    if (Existe_arquivo("Locadora_Clientes.txt")):
        with open("Locadora_Clientes.txt") as arquivo:
            for linha in arquivo:
                infos = linha.split("\n")
                palavras = infos.split(";")
                if (palavras[3] == cpf_cliente):
                    encontrei = True
    if (encontrei == True):
        return True
    else:
        return False

    # Menu´s
def codigos_desnecessarios():
    '''
        #Carros: nome, marca, ano, numero_portas, consumo_litros, kilometragem, lotaçao
        ce = Carro_Esportivo("CS202","mercedes",2020,2,12,0,4,200)
        print(ce)

        fa = Carro_Familiar("Sprinter","mercedes",2013,3,6,87000,10,True)
        print(fa)

        pop = Carro_Popular("uno","fiat",2017,4,12,37000,5)
        print(pop)
        '''
    """
    #moto: nome, marca,ano, cilindragem, consumo, velocidade_maxima
    me = Moto_esportiva("super","yamaha",2013,750,8,220)
    print(me)

    mp = Moto_popular("lambreta","honda",2003,80,4)
    print(mp)
    """
####### Main #########################
if(__name__ == '__main__'):

    #antes de qualquer coisa acontecer eu vou criar as listas de objetos dos veiculos e Pessoas.(fica altamente mais facil e trabalhar assim)
    Lista_de_obj_carros_populares,Lista_de_obj_carros_familiares,Lista_de_obj_carros_esportivos = Cria_listas_de_objetos_CARROS()

    #

    #inicio da rotina principal
    while(True):
        Menu_Principal()
        r = input("Digite o numero da opção desejada: ")
        while r not in "1234":
            r = input("Digite uma opção valida(1, 2 ou 3): ")

        if(r == "1"):#ALugar
            while(True):
                q = input("Cliente ja cadastrado?(s/n)")
                while q.upper() not in "SN":
                    q = input("digite uma opçao valida(s/n): ")
                if(q.upper() == "S"):
                    flag_cpf = False
                    C_cpf = input("Digite o CPF do cliente: ")
                    if(C_cpf != 0):
                        # validar cpf dentro da lista de objetos de Clientes
                        # if(Valida_cpf_cliente()):
                        #     flag_cpf= True
                        # else:
                        #     flag_cpf = False
                        flag_cpf = True
                elif(q.upper() == "N"):
                    t = input("Deseja cadastrar o cliente agora?(S/N) ")
                    while t.upper() not in "SN":
                        t = input("digite uma opçao valida(s/n): ")
                    if(q.upper() == "S"):
                        print("Sessao ainda nao desenvolvida.")
                    #     Cadastrar_Cliete()
                    #     pass
                    # else:
                    #     continue

                if(flag_cpf == True):
                        Menu_aluguel()
                        a = input("Digite o numero da opção desejada: ")
                        while a not in "1234":
                            a = input("tente novamente, digite o numero da opção desejada: ")
                        if(a == "1"):
                            #listar os carros disponiveis
                            Listagem_dos_Carros_Dinponiveis()
                            break
                        elif(a == "2"):
                            # listar motos
                            break
                        elif(a == "3"):
                            # listar barcos
                            break
                        elif(a == "4"):
                            q = input("Deseja realmente sair do 'Menu Alugar'?(s/n)")
                            while q.upper() not in "SN":
                                q = input("digite uma opçao valida(s/n): ")
                            if (q.upper() == "S"):
                                # fechar o arquivo
                                print("Voltando ao menu principal...")
                                break
                            else:
                                print("*" * 42)
                                continue


        if(r == "2"):#Devolver
            Menu_devoluçao()
            #na devoluçao o atendente primeiro diz oq vais ser devolvido
            # depois ele da o cpf ou placa do veiculo a ser devolvido

        if(r == "3"):
            #analize dos arquivos
            pass

        if(r == "4"):#Sair
            q = input("Deseja realmente encerrar o programa?(s/n)")
            while q.upper() not in "SN":
                q = input("digite uma opçao valida(s/n): ")
            if(q.upper() == "S"):
                #fechar o arquivo
                print("Encerrando o programa...")
                break
            else: print("Voltando ao menu principal...")




