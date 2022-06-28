from class_estoque import *
#from class_deposito import *

c = 0
class Menu:
    def  __init__(self):
        Estq = Estoque()
        
        
        while True:   
            entrada = input('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ \n•1->Cadastro de produto. \n•2->Listar todos os Produtos.  \n•3->Listar produto especifico.  \n•4->Alterar Desc/nome do produto.    \n■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ \n----------------------------- -----------------------------\n•0->Exit.\nFaça sua escolha: ')
            Estq.sumiu()
            if entrada == '1':
                Estq.cadastrar_produto()
                
            if entrada == '2':
                Estq.listar_tudo()
            if entrada == '3':
                Estq.listar_unidade()
            if entrada == '4':
                Estq.alter_produto()
            if entrada == '0':
              print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
              print('••••••Processo Encerrado•••••')
              print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
              break
         
               

    

    



