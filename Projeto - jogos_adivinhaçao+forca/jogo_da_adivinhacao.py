
import random

def jogar():
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

      '''
      Update de 13/10/21
      Para evitar erros de entrada eu vou trabalhar com listas de string
      dessa forma quando o usuario colocar 'h' na entrada ou qualquer outro
      caractere do teclado, o jogo nao vai dar erro, so vai pedir que ele
      de uma entrada valida.
      '''
      lista_de_numeros = []
      for numb in range(1,101):
            numb = str(numb)
            lista_de_numeros.append(numb)
      #print(lista_de_numeros)

      print("Escolha o nivel de dificuldade do jogo\n(1)Facil (2)Medio (3)Dificil")
      dificuldade = input("digite sua escolha: ")
      while(dificuldade!= "1" and dificuldade!="2" and dificuldade!="3"):
            dificuldade = input("entrada invalida, tente novamente: ")

      if(dificuldade == "1"):
            total_de_tentativas = 10
      elif(dificuldade == "2"):
            total_de_tentativas = 7
      elif(dificuldade == "3"):
            total_de_tentativas = 3

      total_de_pontos = 1000
      acertou = False
      tt = 1
      while(acertou == False and tt != total_de_tentativas+1):
            if(tt <= total_de_tentativas):
                  print()
                  if(tt == total_de_tentativas):
                        print("ULTIMA TENTATIVA!")
                  else:
                        print("Tentetaiva",tt,"de",total_de_tentativas)

            chute = input("digite um numero de 1 a 100: ")
            while(chute not in lista_de_numeros):
                  print("voce deve digitar um numero entre 1 e 100")
                  chute = input("digite um numero de 1 a 100: ")

            # vamos colocar as expreçoes em variaveis pra utiliza-las nos condicionais como true e false
            acertou = numero_secreto == int(chute)
            maior = int(chute) > numero_secreto
            menor = int(chute) < numero_secreto

            if(acertou):
                  print("voce acertou!")
                  print("Sua pontuaçao total no final do jogo foi de:",total_de_pontos)
            else:
                  print("voce nao acertou.")
                  if(maior):
                        print("chute maior que o numero secreto")
                        desconto_de_pontos = int(chute) - numero_secreto
                  elif(menor):
                        print("chute menor que o numero secreto")
                        desconto_de_pontos = numero_secreto - int(chute)
                  total_de_pontos = total_de_pontos - desconto_de_pontos

            tt = tt + 1


      print()
      print("*"*12,end="")
      print(" Fim do jogo. ",end="")
      print("*"*12)


if(__name__ == "__main__"):
      jogar()
'''
Como esse "__name__" funciona?
essa variavel 'name' é colocada automaticamente
pelo python quando se inicia um arquivo 
quando o arquivo esta sendo chamado por outro arquivo 
essa variavel '__name__' recebe outro valor,
mas quando voce esta executando o arquivo original, por 
sua vez, a variavel recebe o valor "__main__" dizendo que 
o arquivo que esta sendo executado, no csso o 'jogo_da_adivinhaçao'
é o main!
'''