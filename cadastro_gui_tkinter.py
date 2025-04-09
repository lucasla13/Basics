#Bicliotecas de GUI - Interface Grafica
import tkinter as tk

#Nomeando variaveis
etd_nome = []
etd_idade = []
dicionario = dict()

#Definições de ação
#Botão Avançar
def avancar():
    try:
        #Int: converte um valor para número inteiro, se possível.
        qtd = int(entrada.get())
    except ValueError:
        print("Digite um número válido")
        return
    #Range: gera uma sequência de números inteiros, usada geralmente para laços de repetição (for).
    for i in range(qtd):
        tk.Label(janela, text=f"Nome da pessoa{i+1}:").pack()
        entry_nome = tk.Entry(janela)
        entry_nome.pack()
        #Append: adiciona um item (entry) ao fim da lista (etd). 
        etd_nome.append(entry_nome)

        tk.Label(janela, text=f"Idade da pessoa {i+1}:").pack()
        entry_idade = tk.Entry(janela)
        entry_idade.pack()
        #Append: adiciona um item (entry) ao fim da lista (etd). 
        etd_idade.append(entry_idade)

    btn_salvar = tk.Button(janela, text="Salvar", command=salvar)
    btn_salvar.pack()

#Botão Salvar
def salvar():
    #Zip: combina elementos de múltiplas listas (ou iteráveis) em pares, formando duplas com elementos de mesma posição.
    for entry_nome, entry_idade in zip(etd_nome, etd_idade):
        nome = entry_nome.get()
        idade = int(entry_idade.get())
        dicionario[nome] = idade
    soma = 0
    for idade in dicionario.values():
        soma += idade
    velho = max(dicionario, key=dicionario.get)
    media = soma / len(dicionario)

    print(f"Media de idade: {media}")
    print(f"Mais velho: {velho}")


#Janela Inicial
janela = tk.Tk()
janela.title("Cadastro de Pessoas")

label = tk.Label(janela, text="Quantas pessoas deseja cadastrar?")
entrada = tk.Entry(janela)
#Command: no Tkinter, command é usado para ligar um botão (ou widget similar) a uma função que será executada quando o botão for clicado.
btn_a = tk.Button(janela,text="Avançar", command=avancar)
btn_b = tk.Button(janela, text="Cancelar", command=janela.destroy)

#Pack: organiza os widgets na interface gráfica, alinhando-os automaticamente em blocos (vertical ou horizontalmente).
label.pack()
entrada.pack()
btn_a.pack()
btn_b.pack()

#Mainloop: mantém a interface gráfica ativa, esperando e respondendo a eventos do usuário.
janela.mainloop()