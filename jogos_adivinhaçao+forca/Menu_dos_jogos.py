'''
Original post: usando este metodo eu consigo fazer o menu rodar,
mas depois do jogador ser transferido para o arquivo
do jogo correspondente ele nao retorna. por esse motivo
é mais facil fazer do jeito que o professro ensinou, que
sera o metodo efetivamente utilizado neste programa

UPDATE: o meu metodo funciona igual ao do professor,
a unica diferença é que o dele usa metodos e o meu nao
tecnicamente falando, o meu fica ate menos trabalho de
codar. ps:lembrar que pro meu metodo rodar eu tenho que
desfarzer as mudanças que o prof fez nos arquivos dos
jogos ->colocou os codigos em formato de modulo<-

def forca():
    import jogo_da_forca

def adivinhacao():
    import jogo_da_adivinhacao
'''

import jogo_da_adivinhacao
import jogo_da_forca

escolha = 0
while(escolha != 3):
    print("*"*30)
    print("Bem vindo ao Menu de Jogos")
    print("*"*30)
    print("Escolha qual jogo voce quer jogar:\n(1)Jogo da Adivinhação\n(2)Jogo da Forca\n(3)Sair(Encerrar)")
    escolha = int(input("digite o numero da sua escolha: "))

    if(escolha == 1):
        print("inicializando o Jogo da Adivinhação...")
        jogo_da_adivinhacao.jogar()
        #adivinhacao()
    elif(escolha == 2):
        print("inicializando o Jogo da Forca...")
        jogo_da_forca.jogar()
        #forca()
    elif(escolha == 3):
        print("Encerrando o programa...")
        break


''' 
UPDATE: oq eu escrevi aqui ta certo, mas ao mesmo tempo errado =),
nao é so usando modulos que funciona desse jeito, apesar de ficar mais
bonito
Original post: utilizando este metodo de import, alem de colocar 
os programas dos jogos em formato de 'def' ou medulo 
eu posso chamar eles e depois voltar ao menu quando 
a funçao chamada chegar. 
'''

