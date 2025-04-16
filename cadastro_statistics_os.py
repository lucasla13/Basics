# -- IMPORTAÇÕES --
import os #os: Limpar a tela do terminal./Criar, deletar ou navegar por pastas e arquivos./Obter informações do sistema.
import statistics as stats
import time
import csv

# -- COLETA DE DADOS --
def coletar_pessoa(dados: dict[str, int]) -> dict[str, int]:
        nome = input('Nome: ')
        idade = input('Idade: ')

        try:
            idade = int(idade)
            dados[nome] = idade
        except ValueError:
            print('Idade inválida')
        return dados

# -- CÁLCULOS --
def estatisticas(dados: dict[str, int]):
    def calcular_media()->float:
        return stats.mean(dados.values()) #Chama stats para executar a função mean, no dict definido como dados, calculando os valores (value)

    def calcular_mediana()->float:
        return stats.median(dados.values())

    def mais_velhos()-> list[str]:
        return [nome for nome, idade in dados.items() if idade >= 18]

    def mais_jovens()-> list[str]:
        return [nome for nome, idade in dados.items() if idade < 18]
    return {
        'media': calcular_media(),
        'mediana': calcular_mediana(),
        'mais_velho': mais_velhos(),
        'mais_jovens': mais_jovens()
    }

# -- MENU --
def menu():
        print( "\n-- MENU --") #\n: quebra de linha
        print('1 - Coletar dados')
        print('2 - Mostrar dados')
        print('3 - Sair')

        opcao = input('Escolha uma opção: ') #input(): sempre retorna texto (string), então "1" é diferente de 1

        os.system('cls' if os.name == 'nt' else 'clear') #Limpa a tela do terminal (Windows usa 'cls', outros usam 'clear')

        return opcao

def main(opcao):
        dados = carregar_csv("dados.csv")
        while True:
            if opcao == "1":
                coletar_pessoa(dados)
                opcao = menu()
            
            elif opcao == "2":
                if dados:
                    resultados = estatisticas(dados)
                    print("\n -- ESTATÍSTICAS --")
                    print("Média:", resultados['media']) #f'': é uma f-string (formatação de string), usada para inserir variáveis dentro do texto.Exemplo: print(f'Média de idade: {stats.mean(dados.values())}')
                    print("Mediana:", resultados['mediana'])
                    print("Mais velho(s):", resultados['mais_velho'])
                    print("Mais joven(s):", resultados['mais_jovens'])
                else:
                    print("Nenhum dado disponível ainda.")
                opcao = menu()
            elif opcao == "3":
                salvar_csv(dados)  # salvar antes de sair
                print("Finalizando programa")
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
                break
            else:
                print("Opção inválida")

# -- EXPORTAR CSV --
def salvar_csv(dados: dict[str, int], nome_arquivo: str= "dados.csv"):
    with open(nome_arquivo, mode='w', newline='') as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow(["Nome","Idade"])

        for nome, idade in dados.items():
            writer.writerow([nome, idade])
    print(f"Dados salvos em {nome_arquivo}")

# -- CARREGA CSV --
def carregar_csv(nome_arquivo: str) -> dict[str, int]:
    dados = {}
    try:
         with open(nome_arquivo, mode='r') as arquivo:
              reader = csv.reader(arquivo)

              next(reader)

              for row in reader:
                   nome, idade = row
                   dados[nome] = int(idade)
    except FileNotFoundError:
         print(f"Arquivo {nome_arquivo} não encontrado")
    return dados

# -- EXECUÇÃO --
opcao = menu()  # obtém a escolha do usuário no menu
main(opcao)     # executa a lógica principal com base na escolha
