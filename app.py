import os

restaurantes = [{'nome': 'Sushi Karim', 'categoria': 'Japonesa', 'ativo': False}, {'nome': 'SubWay', 'categoria': 'Fast Food', 'ativo': True}, {'nome': 'MC Donalds', 'categoria': 'Fast Food', 'ativo': True}, {'nome': 'Burger King', 'categoria': 'Fast Food', 'ativo': True}]

def exibir_nome_do_programa() :
    '''Esta função é responsável por exibir o título do sistema'''
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      """)

def exibir_opcoes():
    '''Esta função é responsável por exibir as opções do sistema'''
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair\n')

def finalizar_app() :
    '''Esta função é responsável por finalizar o sistema'''
    exibir_subtitulo('Finalizar App')

def voltar_ao_menu():
    '''Esta função é responsável por retornar ao menu principal'''
    input('Aperte ENTER para voltar ao menu principal\n')
    main()

def opcao_invalida() :
    '''Esta função é responsável por alertar ao usuário que a opção selecionada não existe'''
    print('Opção Inválida!\n')
    voltar_ao_menu()

def exibir_subtitulo(texto):
    '''Esta função é responsável por formatar os subtítulos das telas'''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante() :
    ''' Essa função é responsável por cadastrar um novo restaurante'''
    
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'\nO restaurante {nome_do_restaurante} foi cadastrado e inserido na categoria {categoria} com sucesso!\n')
    voltar_ao_menu()

def listar_restaurantes():
    ''' Esta função é responsável por listar os restaurantes cadastrados'''
    exibir_subtitulo('Lista de restaurantes')
    
    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Status'}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    voltar_ao_menu()

def alternar_estado_restaurante():
    '''Esta função é responsável por alternar de estado o restaurante'''
    exibir_subtitulo('Alternar estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if restaurante['nome'] == nome_restaurante:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            estado = 'ativado' if restaurante['ativo'] else 'desativado'
            print(f'\nO restaurante {nome_restaurante} foi {estado} com sucesso!\n')
    if not restaurante_encontrado:
        print('O restaurante não foi localizado no sistema. Ele já foi cadastrado?')
    voltar_ao_menu()

def escolher_opcoes() :
    '''Esta função é responsável pela seleção de tela do sistema'''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1 :
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2 :
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:        
        opcao_invalida()
        
def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()
    
if __name__ == '__main__':
    main()