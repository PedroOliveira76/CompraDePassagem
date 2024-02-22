class DadosPassagemPrinter:
    def __init__(self, lista_dados):
        self.__lista_dados = lista_dados

    # Classe criada para mostrar todas as passagem comprada pelo o usuário atual do programa
    # De acordo com a opção da Tela_Principal
    def imprimir_dados_passagem(self):

        #verifica se a lista está vazia
        if not self.__lista_dados:
            print('Nenhuma passagem encontrada!')

        else:
            c = 1
            for dados in self.__lista_dados:
                nome_comprador, tipo_pagamento, country, departure_time, valor = dados
                print('-' * 15, 'Dados Passagem', '-' * 15)
                print(f'Número da compra: {c}\n'
                      f'Nome: {nome_comprador}\n'
                      f'Voo: {country}\n'
                      f'Horário de partida: {departure_time}\n'
                      f'Tipo pagamento: {"Cartão" if tipo_pagamento == 1 else "Pix"}\n'
                      f'Valor: {valor}\n')
                print('-' * 45)
                c+=1
            return self.__lista_dados
