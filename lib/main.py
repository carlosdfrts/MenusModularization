# Importando módulos necessários
from interface import * # Módulo com funções de interface (menu, cabeçalho).
from arquivo import * # Módulo com funções para manipulação de arquivos.
from time import sleep # Módulo para introduzir atrasos.

# Definindo o nome do arquivo.
arquivo = 'ficha.txt'

# Verificando se o arquivo existe, se não existir, cria um com o nome informado.
if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

# Loop principal do programa.
while True:
    # Apresentando um menu de opções para o usuário.
    resposta = menu(['Listar Pessoas', 'Cadastrar Pessoas', 'Sair do Sistema'])

    if resposta == 1:
        # Opção de listar o conteúdo do arquivo.
        lerArquivo(arquivo)
    elif resposta == 2:
        # Opção para cadastrar uma nova pessoa.
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arquivo, nome, idade)
    elif resposta == 3:
        # Opção para sair do sistema.
        cabeçalho('\033[33mSaindo do sistema...\033[m')
        sleep(2)
        cabeçalho('\033[32mVolte sempre! :D\033[m')
        break
    else: 
        # Mensagem de erro para opção inválida.
        print('\033[031mERRO! Opção inválida, digite uma opção válida.\033[m')

    # Introduzindo um atraso de 2 segundos entre as operações.
    sleep(2)
