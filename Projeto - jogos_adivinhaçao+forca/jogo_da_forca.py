import random

def tenta_abrir_arquivo(nome):
    try:
        a = open(nome,'r')
    except FileNotFoundError:
        return False
    else:
        return True

def cria_novo_arquivo(nome):
    try:
        a = open(nome, 'wt+')
    except:
        print(">>Ocorreu um erro na criaçao do arquivo")
    else:
        print(">Arquivo {} criado com sucesso<".format(nome))

def fecha_o_arquivo(nome):
    try:
        nome.close()
    except:
        print(">>Ocorreu um erro na hora de fechar o arquivo.")
    else:
        print(">Arquivo fechado com sucesso.<")

def dados_default():
    lista = ["laranja", "uva", "pera", "banana", "abacaxi" , "manga" , "caju"]
    return lista

def jogar():
    print("*"*30)
    print("Bem vindo ao jogo da Forca!")
    print("*"*30)
    print(" ->regras: Voce tera 7 tentativas para acertar uma palavra secreta,\na cada chance errada voce perde uma tentativa.")
    print("*"*30)

    #nome do arquivo: palavras.txt
    nome_arquivo = "palavras.txt"
    arquivo_ok = False
    if(tenta_abrir_arquivo(nome_arquivo)):
        arquivo_ok = True
        print(">Arquivo carregado com sucesso<")
    else:
        print("Arquivo nao encontrado, devo criar um novo arquivo 'palavras.txt' e alimenta-lo com dados default?")
        resp = input("S/N: ").lower()
        while(resp not in ["s","n"]):
            resp = input("entrada invalida!\nS/N: ")
        if(resp == "s"):
            cria_novo_arquivo(nome_arquivo)
            if(tenta_abrir_arquivo(nome_arquivo)):
                arquivo_ok = True
                lista = dados_default()
                with open(nome_arquivo,"w") as arquivo:
                    for i in lista:
                        arquivo.write(f"{i}\n")
        else:
            arquivo_ok = False
            print("O jogo nao pode começar sem um arquivo carregado e sera encerrado agora...")

    if(arquivo_ok == True):
        lista2 = []
        with open(nome_arquivo,"r") as arquivo:
            for linha in arquivo:
                lista2.append(linha.strip().replace("\n",""))

        palavra_secreta = str(lista2[random.randint(0,len(lista2))])
        lista_acertos = ["_" for letra in palavra_secreta] #list_comprehension
        letras_jogadas = "*"
        print("Palavra secreta ->",lista_acertos)
        enforcou = False
        acertou = False
        erros = 7

        while(not enforcou and not acertou):
            chute = input("digite uma letra: ").strip()
            while(chute.lower() in letras_jogadas.lower()):
                letras_jogadas += chute
                print("Voce ja tentou jogar essa letra anteriormente, tente novamente!")
                chute = input("digite uma letra: ").strip()

            if (chute.lower() not in palavra_secreta.lower()):
                print("A letra '{}' nao pertenca a pelavra secreta.\n".format(chute))
                erros -= 1
                letras_jogadas += chute
            else:
                letras_jogadas += chute
                index = 0
                for letra in palavra_secreta:
                    if(letra.upper() == chute.upper()):
                        print("Encontramos a letra '{}' no index {}.".format(chute,index))
                        lista_acertos[index] = letra
                    index = index + 1
                print(lista_acertos)
                if ("_" not in lista_acertos):
                    acertou = True
                    print("Voce venceu o jogo!")
                    #print(letras_jogadas)
                else:
                    print("jogando...\n")
            if(erros == 0):
                enforcou = True
                print(">>>Suas tentativas se esgotaram e voce perdeu o jogo =( .")
            if(lista_acertos.count("_") != 0 and erros != 0):
                if(erros == 1):
                    print("->Ultima tentativa!! e ainda faltam {} letras secretas.".format(lista_acertos.count("_")))
                else:
                    print("->Ainda faltam {} letras secretas e voce tem mais {} tentativas.".format(lista_acertos.count("_"),erros))

        print()
        print("*"*12,end="")
        print(" Fim do jogo, voltando ao menu principal... ",end="")
        print("*"*12)

    fecha_o_arquivo(nome_arquivo)
    #fim

if(__name__ == "__main__"):
      jogar()
#expplicaçao no arquivo 'jogo_da_adivinhaçao'



