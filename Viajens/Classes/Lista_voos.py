import random
import string
import time
class VoosOperações:
    @staticmethod
    def escolherVoo():
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
                for flight in flights_data:
                    print(f' {c} - {flight["country"]} - {flight["departure_time"]} - {flight["Valor"]}')
                    c+=1

                opcao = int(input("Escolha uma opção: "))

                if 1 <= opcao <= len(flights_data):
                    while True:
                        try:
                            print('-' * 15, 'Qual vai ser a forma de pagamento?', '-' * 15)
                            opcao_pagamento = int(input(f'1 - Cartão\n'
                                                        f'2 - Pix\n'
                                                        f'Opção: '))
                            print('-' * 30)

                            textoResultado = VoosOperações.formaPagamento(opcao_pagamento, flights_data[opcao - 1]["Valor"])
                            return textoResultado # Retorna os dados do voo selecionado

                        except ValueError as error:
                            print(f'Error: {error}'
                                  f'Escolha um número!')
                else:
                    print("Opção inválida. Escolha um número entre 1 e", len(flights_data))

            except ValueError as error:
                print(f'Error: {error} \n'
                      f'Escolha um número!')

    @staticmethod
    def formaPagamento(opcao_pagamento, flight_valor):
        while True:
            try:
                match opcao_pagamento:
                    case 1:
                        print('-' * 15, 'Dados do Cartão', '-' * 15)
                        print("Por favor, insira as informações do seu cartão de crédito:")
                        numero_cartao = int(input("Número do cartão: "))
                        nome_titular = str(input("Nome do titular: "))
                        textoResultado = (f'Compra no valor de {flight_valor} no cartão - "{numero_cartao}"'
                                          f'foi aprovada no nome do proprietário: {nome_titular}')
                        return textoResultado
                        pass

                    case 2:
                        sequencia_aleatoria = ''.join(
                            random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(10))

                        print(f'Chave aleatória para o pagamento: {sequencia_aleatoria}')

                        for _ in range(8):
                            print(".", end="", flush=True)  # Imprime um ponto sem nova linha
                            time.sleep(1)  # Pausa por 1 segundo
                        print("\nPix confirmado!")

                        textoResultado = f'Pagamento confirmado no valor de {flight_valor}'

                        return textoResultado

            except ValueError as error:
                print(f'Siga as instruções corretamente!\n'
                      f'Error: {error}')



