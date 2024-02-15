
class Voos_lista:
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
                    print(f' {c} - {flight["country"]} - {flight["departure_time"]}')
                    c+=1
                opcao = int(input("Escolha uma opção: "))
                if 1 <= opcao <= len(flights_data):
                    while True:
                        try:
                            print('-' * 15, 'Qual vai ser a forma de pagamento?', '-' * 15)
                            opcaoPagamento = int(input(f'1 - Cartão\n'
                                                        f'2 - Pix\n'
                                                        f'3 - Deposito\n'
                                                        f'Opção: '))

                            return flights_data[opcao - 1]  # Retorna os dados do voo selecionado
                        except ValueError as error:
                            print(f'Error: {error}'
                                  f'Escolha um número!')
                else:
                    print("Opção inválida. Escolha um número entre 1 e", len(flights_data))

            except ValueError as error:
                print(f'Error: {error} \n'
                      f'Escolha um número!')


if __name__ == '__main__':
    teste = Voos_lista()
    print('-----Cidades------------------Horário------')
    for flight in teste.escolherVoo():
        country = flight["country"]
        time = flight["departure_time"]
        print(f'|{country}|      |{time}|')


