from CompraDePassagem.Viajens.Classes.DadosPrintPassagem import DadosPassagemPrinter


class Cancelar_compra(DadosPassagemPrinter):
    #Iniciação da classe fazendo um Inheritance com DadosPrintPassagem usando o super()
    def __init__(self, lista_dados):
        super().__init__(lista_dados)
        self.__lista_dados = lista_dados

    def cancelar_passagem(self):
        while True:
            try:
                #Utilização do método da classe DadosPrint para exibir a lista de dados da passagem do usuário
                dados = DadosPassagemPrinter(self.__lista_dados)
                lista_dados = dados.imprimir_dados_passagem()

                #Caso a lista esteja vazia entra nesse if para cancelar a operação e voltar ao menu inicial
                if not lista_dados:
                    return f'Nenhuma passagem encontrada'

                #Inicia a variável para começar o loop
                response = True
                while response == True:
                    try:

                        print('-' * 30)
                        #De acordo com os dados mostrado a cima, o usuário irá escolher o número da passagem
                        #Nesse casso o número da passagem está se referindo a posição da tupla de dados na lista
                        opcao_num = int(input('Escolha o número da compra: '))

                        #verifica se a opção escolhida se adequa ao tamanho da lista
                        if 1 <= opcao_num <= len(lista_dados):
                            nome_comprado, tipo_pagamento, pais, departure_time, valor = lista_dados[opcao_num - 1]

                            print('-' * 30)
                            print('A passagem selecionada foi: \n'
                                  f'Titular: {nome_comprado}\n'
                                  f'Tipo do pagamento: {"Cartão" if tipo_pagamento == 1 else "Pix"}\n'
                                  f'Destino da passagem: {pais}')
                            print('-' * 30)

                            opcao = int(input('Deseja cancelar?\n'
                                              '1 - Sim\n'
                                              '2 - Não\n'))
                            print('-' * 30)

                            #Bloco do código feito para remoção da tupla selecionada com os dados
                            if opcao == 1:
                                lista_dados.remove(lista_dados[opcao_num - 1])
                                print('Itens Removido com sucesso')
                                response = False
                            elif opcao == 2:
                                response = False
                            else:
                                print('Escolha o número correto')

                        else:
                            print('Opção inválida')

                    except ValueError as erro:
                        print(f'Ocorreu um erro: {erro} ')

                return 'Cancelar finalizado'

            except ValueError as erro:
                print(erro)
