from Viajens.Classes.Lista_voos import Voos_lista


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
                                  f'4 - Sair\n'
                                  f'Escolha uma opção : '))

                if opcao < 1 or opcao > 4:
                    raise OpcaoInvalidaError('Opção inválida!')

                print('>' * 30)

                match opcao:
                    case 1:
                        resultado = Voos_lista.escolherVoo()

                        print(resultado)
                        pass
                    case 2:
                        pass
                    case 3:
                        pass
                    case 4:
                        pass
            except ValueError as error:
                print(f'Erro: {error}\n Escolha um número!')
            except OpcaoInvalidaError as error:
                print(f'Erro: {error}')


if __name__ == '__main__':
    testeMain = Menu()
    testeMain.mostrar_tela()
