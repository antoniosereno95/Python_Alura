
print("*"*30)
print("Bem vindo ao jogo da adivinhaçao!")
print("*"*30)
print(" ->regras: voce tera 10 chances "
      "de acertar um numero de 0 a 100 gerado automaticamente.")
print("*"*30)

numero_secreto = 42

chute = int(input("digite o seu numero: "))
print("voce digitou",chute)

if(numero_secreto == chute):
      print("voce acertou!")
else:
      print("voce nao acertou.")
print("\nFim do jogo.")