
############# Imports ##############
from Testes_Automatizados_Python.Leilao.Leilao_Classes import Usuario, Lance, Leilao,Avaliador



############# Main #################
if(__name__ == "__main__"):

    leilao = Leilao("Celular")

    gui = Usuario("Gui")
    yuri = Usuario("Yuri")

    lance_do_gui = Lance(gui, 150.0)
    lance_do_yuri = Lance(yuri, 100.0)

    leilao.lista_de_lances.append(lance_do_yuri)
    leilao.lista_de_lances.append(lance_do_gui)

    for lance in leilao.lista_de_lances:
        print(f'O usuario {lance.usuario.nome} deu um lance de {lance.valor}')


