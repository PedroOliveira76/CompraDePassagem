class DadosPassagemPrinter:
    def __init__(self, lista_dados):
        self.__lista_dados = lista_dados

    def imprimir_dados_passagem(self):
        if not self.__lista_dados:
            print('Nenhuma passagem encontrada!')
        else:
            for dados in self.__lista_dados:
                nome_comprador, tipo_pagamento, country, departure_time, valor = dados
                print('-' * 15, 'Dados Passagem', '-' * 15)
                print(f'Nome: {nome_comprador}\n'
                      f'Voo: {country}\n'
                      f'Horário de partida: {departure_time}\n'
                      f'Tipo pagamento: {"Cartão" if tipo_pagamento == 1 else "Pix"}\n'
                      f'Valor: {valor}\n')
                print('-' * 45)
