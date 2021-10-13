
def jogar():
    print("*"*30)
    print("Bem vindo ao jogo da Forca!")
    print("*"*30)
    print(" ->regras: Voce tera 7 tentativas para acertar uma palavra secreta,\na cada chance errada voce perde uma tentativa.")
    print("*"*30)

    palavra_secreta = "banana"
    lista_acertos = ["_", "_", "_", "_", "_", "_"]
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
        if(lista_acertos.count("_") != 0 and erros != 0):
            if(erros == 1):
                print("->Ultima tentativa!! e ainda faltam {} letras secretas.".format(lista_acertos.count("_")))
            else:
                print("->Ainda faltam {} letras secretas e voce tem mais {} tentativas.".format(lista_acertos.count("_"),erros))

    print()
    print("*"*12,end="")
    print(" Fim do jogo. ",end="")
    print("*"*12)


if(__name__ == "__main__"):
      jogar()
#expplicaçao no arquivo 'jogo_da_adivinhaçao'



