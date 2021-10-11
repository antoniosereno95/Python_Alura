'''
Maria acabou de iniciar seu curso de graduação na faculdade de medicina e precisa de sua ajuda para organizar os experimentos de um laboratório o qual ela é responsável. Ela quer saber no final do ano, quantas cobaias foram utilizadas no laboratório e o percentual de cada tipo de cobaia utilizada.

Este laboratório em especial utiliza três tipos de cobaias: sapos, ratos e coelhos. Para obter estas informações, ela sabe exatamente o número de experimentos que foram realizados, o tipo de cobaia utilizada e a quantidade de cobaias utilizadas em cada experimento.

Entrada
A primeira linha de entrada contém um valor inteiro N que indica os vários casos de teste que vem a seguir. Cada caso de teste contém um inteiro Quantia (1 ≤ Quantia ≤ 15) que representa a quantidade de cobaias utilizadas e um caractere Tipo ('C', 'R' ou 'S'), indicando o tipo de cobaia (R:Rato S:Sapo C:Coelho).

Saída
Apresente o total de cobaias utilizadas, o total de cada tipo de cobaia utilizada e o percentual de cada uma em relação ao total de cobaias utilizadas, sendo que o percentual deve ser apresentado com dois dígitos após o ponto.
'''
print("--Experiencias--")

casos = int(input("digite o numero de casos que seram fornecidos: "))
print("modulaçao da entrada: primeiro a quantidade de cobaias usada(de 1 a 15),\nseguida de um espaço em branco e logo depois\na letra que define o tipo de animal utilizado(C,R,S)")
#variaveis
ratos = 0
sapos = 0
coelhos = 0

for i in range(casos):
    print("\nentrada de dados do caso",(i+1))
    #verificaçao da entrada de dados
    ok = True
    while(ok):
        entrada = str(input("digite: "))
        entradas = entrada.split(" ")
        numero = int(entradas[0])
        animal = str(entradas[1])
        if(numero > 15 or numero < 1):
            print("quantia nao aceita tente novamente.")
        elif(animal!='C' and animal!='c' and animal!='S' and animal!='s' and animal!='R' and animal!='r'):
            print("tipo de animal invalido!")
        else:
            ok = False
    #termino da verificaçoa

    if(animal == 'C' or animal == 'c'):
        coelhos = coelhos + numero
    if(animal == 'R' or animal == 'r'):
        ratos = ratos + numero
    if(animal == 'S' or animal == 's'):
        sapos = sapos + numero
#termino da entrada de dados
t = coelhos + ratos + sapos
print("Total: ",t)
print("Total de coelhos:",coelhos)
print("Total de ratos:",ratos)
print("Total de sapos:",sapos)

#calculo das percentagens
p_c = (coelhos*100)/t
p_s = (sapos*100)/t
p_r = (ratos*100)/t
print("Percentual de coelhos:",p_c)
print("Percentual de ratos:",p_r)
print("Percentual de sapos:",p_s)

print("#FIM")