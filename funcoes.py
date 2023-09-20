import pandas as pd
from datetime import datetime
import doctest
import locale

locale.setlocale(locale.LC_ALL, "pt_BR.utf8")

def calculo_digita(data):
    """ Função que calcula o número de dias entre datas dentro de um arquivo texto.

    Parameters
    ----------
    data : string
        Datas no formato especificado "DD de MÊS de ANO - DD de MÊS de ANO"

    Returns
    -------
    int 
        A quantidade de dias entre duas datas

    Teste 1
    >>> calculo_digita("23 de Agosto de 2023 - 18 de Setembro de 2023")
    O número de dias entre essas datas é:  25

    Teste 2
    >>> calculo_digita("18 de Setembro de 2023 - 23 de Agosto de 2023")
    O número de dias entre essas datas é:  25
    """
    
    #Separa as datas
    array = data.split(" - ")
    
    try:
        #Formata em datetime
        data1 = datetime.strptime(array[0], "%d de %B de %Y")
        data2 = datetime.strptime(array[1], "%d de %B de %Y")

        #Como é pedido o dia entre, o menos um remove o dia pertencente as datas passadas no input que estava sendo incluido.
        numero_dias = abs((data2 - data1).days) -1

        print("O número de dias entre essas datas é: ", numero_dias)

    except ValueError:
        print("\n\n\n\n", "#"*10, "ERRO!", "#"*10, )
        print("O formato de datas não está correto! Um exemplo de Formato correto é:\n 18 de Setembro de 2023 - 23 de Agosto de 2023", end="\n")


def calculo_arquivo(file_name):
    """ Função que calcula o número de dias entre datas dentro de um arquivo texto.

    Parameters
    ----------
    file_name : string
        Nome do arquivo recebido no input.

    Returns 
    -------
    int
        Retorna a quantidade de dias entre as datas.

    Teste segunda maior que primeira
    >>> calculo_arquivo("teste1.txt")
    Diferença de dias: 37

    Teste primeira maior que segunda
    >>> calculo_arquivo("teste2.txt")
    Diferença de dias: 37

    Teste resultado zero
    >>> calculo_arquivo("teste3.txt")
    Diferença de dias: 0
    """
    try:
        dados = pd.read_csv(file_name, sep=" - ", header=None, names=["Coluna1", "Coluna2"], engine='python')

        if not dados.empty:
            primeira_data = dados.iloc[0, 0]
            segunda_data = dados.iloc[0, 1]
           
            primeira_data = datetime.strptime(primeira_data, '%d de %B de %Y')
            segunda_data = datetime.strptime(segunda_data, '%d de %B de %Y')

            #Como é pedido o dia entre, o menos um remove o dia pertencente as datas passadas no input que estava sendo incluido.
            quantidade_dias = abs((segunda_data - primeira_data).days)
            if quantidade_dias != 0:
                quantidade_dias -= 1

            print("Diferença de dias:",quantidade_dias)
        else:
            print("O arquivo está vazio!")

    except FileNotFoundError:
        print(f"Arquivo {file_name} não encontrado.")
    except pd.errors.EmptyDataError:
        print("O arquivo está vazio.")
    except ValueError:
        print("O arquivo não contém dados válidos.")

if __name__ == "__main__":
    doctest.testmod(verbose=True)