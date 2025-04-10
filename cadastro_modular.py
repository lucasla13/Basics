#-> dict[str, int] indica que a função retorna um dicionário com chaves do tipo str e valores do tipo int.
#def = define a função
def coletar_dados()-> dict[str, int]:
    resposta = input("Continuar ou 'sair'")
    while resposta != 'sair':
        nome = input('Nome: ')
        idade = input('Idade: ')
        idade = int(idade)
        #Adiciona valores coletados ao dicionario
        dicionario[nome] = idade
        resposta = input("Continuar ou 'sair'")

def calcular_media(dados: dict[str, int]) -> float:
    return sum(dados.values()) / len(dados)
    

def mais_velho(dados: dict[str, int]) -> str:
    return max(dados, key=dados.get)

def mais_jovens(dados: dict[str, int]) -> list[str]:
    return [nome for nome, idade in dicionario.items() if idade < 18]
    #Sem ser List Comprehension
        #menor_idade = min(dicionario.values())
        #jovens = [nome for nome, idade in dicionario.items() if idade < 18]
        #return jovens

def main():
    coletar_dados()
    media = calcular_media()
    velho = mais_velho()
    jovens = mais_jovens()

    #Exibe resultados
    print("\n--- Resultados ---")
    print("Para todos os cadastros:", dicionario)
    print("A média de idade é:", media)
    print("Mais velhos:", velho)
    print("Mais jovens:", jovens)

#X() chama a função
main()