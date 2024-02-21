from interface import *  # Importa funções do módulo 'interface' (contendo 'menu' e 'cabeçalho').

# Função para verificar se um arquivo existe.
def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')  # Tenta abrir o arquivo em modo leitura de texto.
        a.close()  # Fecha o arquivo
    except FileNotFoundError:
        return False  # Retorna False se o arquivo não existe.
    else:
        return True  # Retorna True se o arquivo existe.

# Função para criar um arquivo.
def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')  # Tenta abrir o arquivo em modo escrita de texto ou criar se não existir.
        a.close()  # Fecha o arquivo.
    except:
        print('\033[31mHouve um Erro na criação do arquivo.\033[m')  # Mensagem de erro em vermelho se ocorrer uma exceção.
    else:
        print(f'\033[32mArquivo {nome} criado com sucesso!\033[m')  # Mensagem de sucesso em verde.

# Função para ler e exibir o conteúdo de um arquivo.
def lerArquivo(nome):
    try:
        a = open(nome, 'rt')  # Tenta abrir o arquivo em modo leitura de texto.
    except:
        print('\033[31mErro ao ler o arquivo.\033[m')  # Mensagem de erro em vermelho se ocorrer uma exceção.
    else:
        cabeçalho('PESSOAS CADASTRADAS')  # Chama a função 'cabeçalho' para exibir um cabeçalho.
        for linha in a:
            dado = linha.split(';')  # Divide a linha em partes usando ';' como delimitador.
            dado[1] = dado[1].replace('\n', '')  # Remove a quebra de linha da segunda parte.
            print(f'{dado[0]:<30}{dado[1]:>3} anos')  # Exibe o nome e a idade formatados.
    finally:
        a.close()  # Garante que o arquivo seja fechado mesmo se ocorrer uma exceção.
    input('\nAperte ENTER para continuar.')

# Função para cadastrar novas informações no arquivo
def cadastrar(arquivo, nome='<desconhecido>', idade=0):
    try:
        a = open(arquivo, 'at')  # Tenta abrir o arquivo em modo anexo de texto.
    except:
        print('\033[31mHouve um erro na abertura do arquivo!\033[m')  # Mensagem de erro em vermelho se ocorrer uma exceção.
    else:
        try:
            a.write(f'{nome};{idade}\n')  # Escreve os dados no arquivo.
        except:
            print('\033[31mHouve um erro na hora de escrever os dados!\033[m')  # Mensagem de erro em vermelho se ocorrer uma exceção.
        else:
            print(f'\033[32mNovo registro de {nome} adicionado com sucesso!\033[m')  # Mensagem de sucesso em verde.
            a.close()  # Fecha o arquivo.
