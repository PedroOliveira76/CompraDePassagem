import random
import string
import time
class VoosOperações:
    @staticmethod
    def escolherVoo():
        #dados das viajens

        flights_data = [
            {"country": "Estados Unidos", "departure_time": "2024-02-15 08:00", "Valor": "$500"},
            {"country": "Reino Unido", "departure_time": "2024-02-15 09:30", "Valor": "$1000"},
            {"country": "França", "departure_time": "2024-02-18 10:45", "Valor": "$1000"},
            {"country": "Alemanha", "departure_time": "2024-02-14 12:15", "Valor": "$1500"},
            {"country": "Japão", "departure_time": "2024-02-13 14:00", "Valor": "$2560"},
            {"country": "Austrália", "departure_time": "2024-02-16 16:30", "Valor": "$3000"}

        ]
        print('-' * 15, 'Escolha um voo', '-' * 15)

        while True:
            try:
                c = 1
                # Mostra em ordem os dados dos voos
                for flight in flights_data:
                    print(f' {c} - {flight["country"]} - {flight["departure_time"]} - {flight["Valor"]}')
                    c+=1

                opcao = int(input("Escolha uma opção: "))

                # Faz uma verificação para saber se i valor selecionado está dentre as opções de voo acima
                # Caso contrário ele mostra uma mensagem de error e inicia o loop novamente
                if 1 <= opcao <= len(flights_data):
                    while True:
                        # Lógica para escolher a forma de pagamento, depois ele chama a função formaPagamento, passando os dados necessários
                        try:
                            print('-' * 15, 'Qual vai ser a forma de pagamento?', '-' * 15)
                            opcao_pagamento = int(input(f'1 - Cartão\n'
                                                        f'2 - Pix\n'
                                                        f'Opção: '))
                            print('-' * 30)

                            # As informações selecionadas pelo usuário são armazenadas em lista_dados de acordo com o retorno
                            # da função formaPagamento()
                            nome_coprador, tipo_pagamento = VoosOperações.formaPagamento(opcao_pagamento, flights_data[opcao - 1]["Valor"])

                            #armazena todos os dados necessário na lista
                            lista_dados = (nome_coprador,tipo_pagamento,flights_data[opcao - 1]["country"],
                                                   flights_data[opcao - 1]["departure_time"],
                                                   flights_data[opcao - 1]["Valor"])

                            print('-' * 30)
                            return lista_dados # Retorna os dados do voo selecionado

                        except ValueError as error:
                            print(f'Error: {error}'
                                  f'Ocorreu um error, tente novamente!')

                else:
                    print("Opção inválida. Escolha um número entre 1 e", len(flights_data))
                    print('>' * 30)

            except ValueError as error:
                print(f'Ocorreu um erro tente novamente'
                      f'Error: {error} \n')

    @staticmethod
    def formaPagamento(opcao_pagamento, flight_valor):
        while True:
            try:
                # Tratamento de dados de acordo com a opção escolhida pelo usuário
                match opcao_pagamento:
                    case 1:
                        print('-' * 15, 'Dados do Cartão', '-' * 15)
                        print("Por favor, insira as informações do seu cartão de crédito:")
                        numero_cartao = int(input("Número do cartão: "))
                        nome_titular = str(input("Nome do titular: "))
                        textoResultado = (f'Compra no valor de {flight_valor} no cartão - "{numero_cartao}"'
                                          f' foi aprovada no nome do proprietário: {nome_titular}')
                        print(textoResultado)
                        return nome_titular, opcao_pagamento

                    case 2:
                        sequencia_aleatoria = ''.join(
                            random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(10))

                        print(f'Chave aleatória para o pagamento: {sequencia_aleatoria}')
                        nome_titular_pix = str(input('Digite seu nome: '))
                        # Essa parte do código foi feita apenas para simular o processo do pix
                        for _ in range(2):
                            print(".", end="", flush=True)  # Imprime um ponto sem nova linha
                            time.sleep(1)  # Pausa por 1 segundo
                        print("\nPix confirmado!")

                        print(f'Pagamento confirmado no valor de {flight_valor}')

                        return nome_titular_pix, opcao_pagamento
                        pass

                    # Caso o usuário escolha uma opção diferente das mostradas ele ficando esse case em loop
                    case _:
                        print('>' * 30)
                        print("Opção de pagamento inválida. Por favor, escolha novamente.")
                        opcao_pagamento = int(input(f'1 - Cartão\n'
                                                    f'2 - Pix\n'
                                                    f'Opção: '))

            except ValueError as error:
                print(f'Siga as instruções corretamente!\n'
                      f'Error: {error}')



