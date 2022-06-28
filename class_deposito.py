"""

from class_estoque import *
from class_info import *




info = Info()
estq = Estoque()

class Deposito:
    def __init__(self,quan):
        self.quan = quan
        self.deps = []
       
    



    def exib(self):
        x = len(info.cod)
        i = len(estq.self.armazena)
        for i in range(x):
            if estq.self.armazena[i] == info.cod[x]:
                print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
                print('CODIGO DO PRODUTO:',estq.armazena[i].cod)
                print('NOME DO PRODUTO:',estq.armazena[i].nome)
                print('EMPRESA FORNECEDORA:',estq.armazena[i].fabric)
                print('Quantidade Disponivel de Unidade:',self.quan )
                print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')

#estq.self.quan +=1

    
    def add(self):
        x = len(info.cod)
        i = len(estq.self.armazena)
        for i in range(x):
            if estq.self.armazena[i] != info.cod[x]:
                resp = input('Deseja Adicionar Produto ao estoque? [S/N]')
                if resp == 'S':
                   self.quan +=1
                elif resp == 'N':
                    print('•••Cancelando•••')
                    break
                else:
                    resp = input('Deseja Adicionar Produto ao estoque? [S/N]')
                    


    



"""
    
