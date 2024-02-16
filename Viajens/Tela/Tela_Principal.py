from CompraDePassagem.Viajens.Classes.Lista_voos import VoosOperações

class OpcaoInvalidaError(Exception):
    pass
lista_voos_cliente = []
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
                        lista_voos_cliente.append(resultado)
                        pass
                    case 2:
                        pass
                    case 3:
                        pass
                    case 4:
                        print(lista_voos_cliente)
                        pass
                    case 5:
                        return f'Programa Finalizado'

            except ValueError as error:
                print(f'Erro: {error}\n Escolha um número!')
            except OpcaoInvalidaError as error:
                print(f'Erro: {error}')


if __name__ == '__main__':
    testeMain = Menu()
    testeMain.mostrar_tela()
