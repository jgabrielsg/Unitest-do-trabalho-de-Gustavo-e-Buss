import funcoes

opcao = 0

"23 de Agosto de 2023 - 18 de Setembro de 2023"

print("\nCalcule a quantidade de dias entre duas datas!")

while opcao != 3:

    print("\n----------------MENU----------------")
    print("1 - Digite as datas")
    print("2 - Digite o nome de um arquivo")
    print("3 - Sair\n")
    
    opcao = input("Digite um número: ")

    try:
        opcao = int(opcao)
    except:
        print("Digite un número inteiro")
        continue

    if opcao == 1:
        datas = input("Digite as datas, elas devem estar no formato 'xx de xxxxxx de xxxx - xx de xxxxxx de xxxx' : ")
        funcoes.calculo_digita(datas)
    elif opcao == 2:
        nome_arquivo = input("Digite o nome do arquivo, o arquivo deve conter as datas no formato 'xx de xxxxxx de xxxx - xx de xxxxxx de xxxx' : ")
        funcoes.calculo_arquivo(nome_arquivo)
    elif opcao != 3:
        print("-------------------------------")
        print("Digite um numero válido")

print("Saindo do programa")