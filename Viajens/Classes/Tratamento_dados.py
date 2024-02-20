class Tratamento_dados:

    def __init__(self, dados):
        self.__dados = dados


    def tratar_lista_voo(self):
        for itens in self.__dados:
            print(itens)
