#back-up do conteudo do arquivo "Locadora_carros"
"""
AMG;merecedes-benz;2020;2;14;0;2;320;False\n
TT;audi;2019;2;17;20000;2;280;False\n
Compass;toyota;2018;4;15;25000;7;0;False\n
Sprinter;mercedes;2016;3;16;43000;11;0;True\n
Uno;fiat;2017;4;12;37000;5;0;False\n
Sandero;renault;2016;2;13;48000;5;0;False\n
"""
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
    print("*" * 42)

def Menu_Principal():
    print("*" * 42)
    print("     -Menu de Principal-   ")
    print("1.Alugar.")
    print("2.Devolver.")
    print("3.Menu do Banco de Dados.")
    print("4.Sair")
    print("*" * 42)

def Menu_Banco_de_dados():
    print("*" * 42)
    print("     -Menu do Banco de Dados-   ")
    print("1.Listagens.")
    print("2.Adicionar.")
    print("3.Reescrever.")
    print("4.Sair.")
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
                #print(linhas)'''
                palavras = linhas[0].split(";")
                palavras[8] = palavras[8].removesuffix("\\n")#tratamento da ultima string que vem com esse bagulho feioso ai no final dela.
                #print(palavras)

                if(int(palavras[6])>5 or palavras[8]=="True"):
                    #tem que jogar um try aqui, pq se o tratamento de dados nao estiver correto o objeto nao vai conseguir ser gerado e a api vai crashar
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

def Cria_listas_de_objetos_FUNCIONARIO():
    Lista_de_obj_funcionarios = []
    if(Existe_arquivo("Locadora_Funcionarios.txt")):
        with open("Locadora_Funcionarios.txt","r") as arquivo:
            for line in arquivo:
                linha = line.split("\n")
                #print(linha)
                #linha = ['maria;F;30;12345678;madalena\\n']
                palavras = linha[0].split(";")
                palavras[4] = palavras[4].removesuffix("\\n")
                try:
                    funcionario = Funcionario(str(palavras[0]),str(palavras[1]),int(palavras[2]),str(palavras[3]),str(palavras[4]))
                except: print(">>>tentativa de criar um objeto do tipo FUNCIONARIO fracassada!")
                else:
                    Lista_de_obj_funcionarios.append(funcionario)
    return Lista_de_obj_funcionarios

def Cria_listas_de_objetos_CLIENTES():
    Lista_de_obj_clientes = []

    if(Existe_arquivo("Locadora_Clientes.txt")):
        with open("Locadora_Clientes.txt","r") as arquivo:
            for line in arquivo:
                linha = line.split("\n")
                palavras = linha[0].split(";")
                palavras[5] = palavras[5].removesuffix("\\n")
                try:
                    cliente = Cliente(str(palavras[0]),str(palavras[1]),int(palavras[2]),str(palavras[3]),str(palavras[4]),str(palavras[5]))
                except:
                    print(">>>tentativa de criar um objeto do tipo FUNCIONARIO mal sucedida!")
                else:
                    Lista_de_obj_clientes.append(cliente)
    return Lista_de_obj_clientes

def Valida_cpf_cliente(cpf):
    for objeto in Lista_de_obj_clientes:
        if(objeto.cpf == cpf):
            return True
        else:
            return False

def Login_banco_de_dados(nome,cpf):
    for objeto in Lista_de_obj_funcionarios:
        if(objeto.nome == nome and objeto.cpf == cpf):
            return True
        else:
            return False

def Adicioana_no_Arquivo_de_Carros():
    #nome,marca,ano,numero_portas,consumo_litros,kilometragem,lotaçao,velocidade_maxima,van
    print("~*~"*21)
    print(">cadastro de carro<")
    while(True):
        print("Resposda ao questionario a seguir:")
        nome = input("digite o nome do carro: ")
        nome.strip()
        marca = input("digite a marca do carro: ")
        marca.strip()
        ano = input("digite o ano do carro: ")
        ano.strip()
        numero_portas = input("digite o numero de portas do carro: ")
        numero_portas.strip()
        consumo_litros = input("digite o consumo de conbustivel medio do carro em litros: ")
        consumo_litros.strip()
        kilometragem = input("digite a kilometragem do carro: ")
        kilometragem.strip()
        lotacao = input("digite a lotação maxima do carro: ")
        lotacao.strip()
        print("O carro em questao se encaixa na categoria de carro esportivo?(s/n)")
        r = input()
        while r.upper() not in "SN":
            r = input("(S/n):")
        if(r.upper() == "S"):
            velocidade_max = input("digite a velocidade maxima do carro em km/h: ")
            velocidade_max.strip()
        elif(r.upper() == "N"):
            velocidade_max = 0
        print("o carro em questao se encaixa na categoria van?(s/n)")
        r = input()
        while r.upper() not in "SN":
            r = input("(S/n):")
        if (r.upper() == "S"):
            van = True
        elif (r.upper() == "N"):
            van = False

        flag_erro = False
        #carro familiar
        if(int(lotacao) > 5 or van == True):
            try:
                c = Carro_Familiar(nome,marca,ano,numero_portas,consumo_litros,kilometragem,lotacao,van)
            except:
                print("erro ao tentar criar o objeto carro.")
                flag_erro = True
        #carro esportivo
        if(velocidade_max != 0):
            try:
                c = Carro_Esportivo(nome,marca,ano,numero_portas,consumo_litros,kilometragem,lotacao,velocidade_max)
            except:
                print("erro ao tentar criar o objeto carro.")
                flag_erro = True
        #carro popular
        if (int(lotacao) == 5):
            try:
                c = Carro_Popular(nome, marca, ano, numero_portas, consumo_litros, kilometragem, lotacao)
            except:
                print("erro ao tentar criar o objeto carro.")
                flag_erro = True

        #se der erro no objeto
        if(flag_erro == True):
            t = input("deseja tentar novamente o cadastro?(s/n)")
            while t.upper() not in "SN":
                t = input("(s/n)")
            if(t.upper() == "S"):
                pass
            else:
                break

        #se der tudo certo
        elif(flag_erro == False):
            print("infos:")
            print(c)
            t = input("\ndeseja realmente adicionar essas informaçoes ao arquivo?(s/n)")
            while t.upper() not in "SN":
                t = input("(s/n)")
            if (t.upper() == "S"):
                Tratamento_de_infos_para_por_no_arquivo()
            else:
                t = input("deseja tentar novamente o cadastro?(s/n)")
                while t.upper() not in "SN":
                    t = input("(s/n)")
                if (t.upper() == "S"):
                    pass
                else:
                    break
    print("~*~" * 21)
    #fim

def Adicioana_no_Arquivo_de_Clientes():
    pass

def Adicioana_no_Arquivo_de_Funcionarios():
    pass

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
    Lista_de_obj_funcionarios = Cria_listas_de_objetos_FUNCIONARIO()
    Lista_de_obj_clientes = Cria_listas_de_objetos_CLIENTES()
    #

    #inicio da rotina principal
    #adicionar uma peuqena rotina de login do funcionario.
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
                    C_cpf = str(input("Digite o CPF do cliente: "))
                    if(Valida_cpf_cliente(C_cpf)):
                        flag_cpf = True
                        print(">Cliente encontrado em nossos arquivos<")
                    else:
                        flag_cpf = False

                elif(q.upper() == "N"):
                    t = input("Deseja cadastrar o cliente agora?(S/N) ")
                    while t.upper() not in "SN":
                        t = input("digite uma opçao valida(s/n): ")
                    if(q.upper() == "S"):
                        Adicioana_no_Arquivo_de_Clientes()
                    else:
                        continue

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
            # depois ele da o cpf ou placa do veiculo(que nao tem variavel implementada ainda) a ser devolvido

        if(r == "3"):#opçoes do banco de dados
            print(">ACESSO RESTRITO, LOGIN NECESSARIO<")
            F_nome = str(input("Digite seu nome:"))
            F_cpf = str(input("Digite seu cpf:"))
            if(Login_banco_de_dados(F_nome,F_cpf) == False):
                print("*" * 42)
                print("Acesso negado, area designidade somente para funcionarios cadastrados.")
                print("*" * 42)
            else:
                print("Acesso consedido...")
                while(True):
                    Menu_Banco_de_dados()
                    opçao = input("Digite a opção desejada: ")
                    while opçao not in "1234":
                        opçao = input("Digite uma opção valida(1,2,3,4): ")

                    if(opçao == "1"):#listagem
                        print("Desaja que seja listada que tipo de arquivo?")
                        print("1.carros\n2.clientes\n3.funcionarios")#depois implementar o resto das opçoes
                        op = input("Digite sua escolha: ")
                        while op not in "123":
                            op = input("Digite sua escolha(1,2 ou 3): ")
                        if(op == "1"):
                            #depois arrumar isso aqui, pq um carro pode nao estar disponivel mas ele tem que aparecer na listagem do banco de dados.
                            print("-"*42)
                            Listagem_dos_Carros_Dinponiveis()
                            print("-" * 42)
                        elif(op == "2"):
                            print("-" * 42)
                            for ob in Lista_de_obj_clientes:
                                print(ob)
                            print("-" * 42)
                        elif(op == "3"):
                            print("-" * 42)
                            for ob in Lista_de_obj_funcionarios:
                                print(ob)
                            print("-" * 42)

                    elif(opçao == "2"):#adicionar
                        print("onde desaja adicionar dados?")
                        print("1.carros\n2.clientes\n3.funcionarios")# depois implementar o resto das opçoes
                        op = input("Digite sua escolha: ")
                        while op not in "123":
                            op = input("Digite sua escolha(1,2 ou 3): ")
                        if (op == "1"):
                            Adicioana_no_Arquivo_de_Carros()
                        elif (op == "2"):
                            Adicioana_no_Arquivo_de_Clientes()
                        elif (op == "3"):
                            Adicioana_no_Arquivo_de_Funcionarios()

                    elif(opçao == "3"):#modificar
                        #1 objeto modificado por vez
                        #ficar de olho pois se eu modificar a velo maxima ou o atributo van, ai terei de tirar o objeto de uma lista e arquivo e colocar no outro arquivo e na outra lista !!!!
                        pass
                    elif(opçao == "4"):
                        q = input("Deseja realmente sair do 'Menu do Banco de Dados'?(s/n)")
                        while q.upper() not in "SN":
                            q = input("digite uma opçao valida(s/n): ")
                        if (q.upper() == "S"):
                            print("Voltando ao menu principal...")
                            break
                        else:
                            print("*" * 42)
                            continue


        if(r == "4"):#Sair
            q = input("Deseja realmente encerrar o programa?(s/n)")
            while q.upper() not in "SN":
                q = input("digite uma opçao valida(s/n): ")
            if(q.upper() == "S"):
                #fechar o arquivo
                print("Encerrando o programa...")
                break
            else: print("Voltando ao menu principal...")
        #fim da rotina principal