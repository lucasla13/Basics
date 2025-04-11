# -- IMPORTAÇÕES --
#os: Limpar a tela do terminal./Criar, deletar ou navegar por pastas e arquivos./Obter informações do sistema.
import os
import statistics as stats
import time

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
        #Chama stats para executar a função mean, no dict definido como dados, calculando os valores (value)
        return stats.mean(dados.values())

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
    dados = {}
    while True:

        #\n: quebra de linha
        print( "\n-- MENU --")
        print('1 - Coletar dados')
        print('2 - Mostrar dados')
        print('3 - Sair')

        #input(): sempre retorna texto (string), então "1" é diferente de 1
        opcao = input('Escolha uma opção: ')

        if opcao == "1":
            #Limpa a tela do terminal (Windows usa 'cls', outros usam 'clear')
            os.system('cls' if os.name == 'nt' else 'clear')

            coletar_pessoa(dados)

         #f'': é uma f-string (formatação de string), usada para inserir variáveis dentro do texto.
            #print(f'Média de idade: {stats.mean(dados.values())}')
        elif opcao == "2":
            if dados:
                resultados = estatisticas(dados)
                print("\n -- ESTATÍSTICAS --")
                print("Média:", resultados['media'])
                print("Mediana:", resultados['mediana'])
                print("Mais velho(s):", resultados['mais_velho'])
                print("Mais joven(s):", resultados['mais_jovens'])
            else:
                print("Nenhum dado disponível ainda.")
        elif opcao == "3":
            print("Finalizando programa")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        else:
            print("Opção inválida")

# -- EXECUÇÃO --
menu()