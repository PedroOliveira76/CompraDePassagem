from CompraDePassagem.Viajens.Classes.DadosPrintPassagem import DadosPassagemPrinter
class Cancelar_compra(DadosPassagemPrinter):
    def __init__(self, tupla):
        self.__lista_dados = tupla

    def cancelar_passagem(self):
        while True:
            try:
                dados = DadosPassagemPrinter(self.__lista_dados)
                dados.imprimir_dados_passagem()
                return 'Escolha outra opção'
            except ValueError as erro:
                print(erro)


if __name__ == '__main__':
    lista = [('dados1', 'dados2', 'a', 'b', 'c'), ('dados3', 'dados4', 'd', 'e', 'f')]
    teste = Cancelar_compra(lista)
    teste.cancelar_passagem()
