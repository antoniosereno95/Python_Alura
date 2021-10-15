
class Data:
    def __init__(self,dia,mes,ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formatar(self):
        print("{}/{}/{}".format(self.dia,self.mes,self.ano))


if(__name__=="__main__"):
    from data import Data
    data_teste = Data(15,10,2021)
    data_teste.formatar()