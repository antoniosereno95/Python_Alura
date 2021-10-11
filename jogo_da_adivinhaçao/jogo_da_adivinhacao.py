
import random

print("*"*30)
print("Bem vindo ao jogo da adivinhaçao!")
print("*"*30)
print(" ->regras: voce tera 10 chances "
      "de acertar um numero de 0 a 100 gerado automaticamente.")
print("*"*30)

'''
#gerando meu numero ramdom
numero_secreto = 0
while(numero_secreto<1 or numero_secreto>100):
      numero_secreto = int(round(random.random()*100))
      print("O numero secreto é:",numero_secreto)
'''
#todo esse bloco de codigo pode ser trocado pela funçao
numero_secreto = random.randrange(1,101)
print("O numero secreto é:",numero_secreto)
##
total_de_tentativas = 10
acertou = False

while(acertou == False and total_de_tentativas != 0):
      if(total_de_tentativas < 10):
            print("\ntentativa:",11-total_de_tentativas)
            if (11 - total_de_tentativas == 10): print("ULTIMA TENTATIVA!")

      chute = int(input("digite um numero de 1 a 100: "))
      if(chute < 1 or chute > 100):
            print("voce deve digitar um numero entre 1 e 100")
            continue
      else: print("voce digitou", chute)

      # vamos colocar as expreçoes em variaveis pra utiliza-las nos condicionais como true e false
      acertou = numero_secreto == chute
      maior = chute > numero_secreto
      menor = chute < numero_secreto

      if(acertou):
            print("voce acertou!")
      else:
            print("voce nao acertou.")
            if(maior):print("chute maior que o numero secreto")
            elif(menor):print("chute menor que o numero secreto")
      total_de_tentativas = total_de_tentativas - 1

print("Fim do jogo.")
