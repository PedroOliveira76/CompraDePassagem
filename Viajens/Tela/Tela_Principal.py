from CompraDePassagem.Viajens.Classes.Cancelar_compra import Cancelar_compra
from CompraDePassagem.Viajens.Classes.Lista_voos import VoosOperações
from CompraDePassagem.Viajens.Classes.DadosPrintPassagem import DadosPassagemPrinter
lista_dados = []
class OpcaoInvalidaError(Exception):
    pass

class Menu:
    def mostrar_tela(self):
        while True:
            try:
                print('>' * 30)
                opcao = int(input(f'1 - Lista de voos \n'
                                  f'2 - Cancelar compra \n'
                                  f'3 - Política de reembolso \n'
                                  f'4 - Visualizar Passagem \n'
                                  f'5 - Sair\n'
                                  f'Escolha uma opção : '))

                if opcao < 1 or opcao > 5:
                    raise OpcaoInvalidaError('Opção inválida!')

                print('>' * 30)

                match opcao:
                    case 1:
                        resultado = VoosOperações.escolherVoo()
                        lista_dados.append(resultado)

                    case 2:
                        cancelador = Cancelar_compra(lista_dados)
                        cancelador.cancelar_passagem()

                    case 3:
                        print(f'Política de Reembolso: \n\n'
                              f'1. Reembolso para Pagamentos com Cartão: \n'
                              f'- O reembolso será processado de volta para o mesmo cartão utilizado na compra.\n'
                              f'- Tempo de processamento: 5-10 dias úteis.\n'
                              f'- Valor reembolsado: mesmo valor pago na compra, menos taxas de processamento.\n\n'
                              f'2. Reembolso para Pagamentos com Pix:\n'
                              f'- O reembolso será processado de volta para a conta bancária do cliente.\n'
                              f'- Tempo de processamento: geralmente em minutos a horas.\n'
                              f'- Valor reembolsado: mesmo valor pago na compra, sem taxas adicionais.\n')

                    case 4:
                        exibirPassagens = DadosPassagemPrinter(lista_dados)
                        exibirPassagens.imprimir_dados_passagem()

                    case 5:
                        return f'Programa Finalizado'

            except ValueError as error:
                print(f'Erro: {error}\n Escolha um número!')
            except OpcaoInvalidaError as error:
                print(f'Erro: {error}')

