


from class_info import *
#listar/buscar

#from class_deposito import *


#dep = Deposito()

class Estoque:
    def __init__(self):
        self.armazena = []


#=================================================================================================================
                                          #AVISO 
#=================================================================================================================
#Eu deixei sem a função de quantidade por que eu ainda não terminei a função de compra e depósito, a minha tentativa ta toda comentada por ai...


#(self,cod,nome,fabric,quan

    def cadastrar_produto(self):
         print(' ----------------------------- -----------------------------\n■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
         armaz_cod = input('Informe o codigo do produto:')
         armaz_nome =  input('Informe a descrição/nome do produto:')
         armaz_fabric  = input('Informe a empresa fornecedora:')
    
         self.armazena.append(Info(cod=armaz_cod, nome=armaz_nome,fabric=armaz_fabric))
         print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ \n  ----------------------------- -----------------------------')




    def listar_tudo(self):
        for i in range(len(self.armazena)):
            print( f'   ----------------------------- ----------------------------- \n ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ \n /|CODIGO CADASTRADO',self.armazena[i].cod,'   \n /|NOME:',self.armazena[i].nome,'        \n /|FORNECEDOR:',self.armazena[i].fabric, '\n■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ \n ----------------------------- -----------------------------')   


    def listar_unidade(self):
        resp = input('Insira o codigo desejado:')
        for i in range(len(self.armazena)):
            if resp == self.armazena[i].cod:
                print( f'   ----------------------------- ----------------------------- \n■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ \n /|CODIGO CADASTRADO',self.armazena[i].  cod,'   \n /|NOME:',self.armazena[i].nome,'        \n /|FORNECEDOR:',self.armazena[i].fabric,    '\n■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ \n----------------------------- -----------------------------')   
         
        if resp == '':
          for i in range(len(self.armazena)):
            print( f'   ----------------------------- ----------------------------- \n ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ \n /|CODIGO CADASTRADO',self.armazena[i].cod,'   \n /|NOME:',self.armazena[i].nome,'        \n /|FORNECEDOR:',self.armazena[i].fabric, '\n■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ \n ----------------------------- -----------------------------')   



    def alter_produto(self):
        resp = input('Insira o codigo desejado:')
        for i in range(len(self.armazena)):
            if resp == self.armazena[i].cod:
               self.armazena[i].nome = input('Atualize a Descrição:')
            else:
                break
            



    def sumiu(self):
        print(500*'\n')