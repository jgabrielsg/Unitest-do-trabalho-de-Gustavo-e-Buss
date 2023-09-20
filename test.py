import unittest
import doctest
import locale
import os

from funcoes import calculo_digita, calculo_arquivo

locale.setlocale(locale.LC_ALL, "pt_BR.utf8")

class TestCalculoFuncoes(unittest.TestCase):
    # Não funciona sem return*
    def test_calculo_digita(self):
        resultado = calculo_digita("23 de Agosto de 2023 - 18 de Setembro de 2023")
        self.assertEqual(resultado, "O número de dias entre essas datas é:  25")

        resultado = calculo_digita("18 de Setembro de 2023 - 23 de Agosto de 2023")
        self.assertEqual(resultado, "O número de dias entre essas datas é:  25")


    # Funciona corretamente
    def test_calculo_arquivo(self):
        with open("teste1.txt", "w") as f:
            f.write("23 de Agosto de 2023 - 18 de Setembro de 2023\n")

        with open("teste2.txt", "w") as f:
            f.write("18 de Setembro de 2023 - 23 de Agosto de 2023\n")

        with open("teste3.txt", "w") as f:
            f.write("10 de Janeiro de 2022 - 10 de Janeiro de 2022\n")

        resultado = calculo_arquivo("teste1.txt")
        self.assertEqual(resultado, "Diferença de dias: 25")

        resultado = calculo_arquivo("teste2.txt")
        self.assertEqual(resultado, "Diferença de dias: 25")

        resultado = calculo_arquivo("teste3.txt")
        self.assertEqual(resultado, "Diferença de dias: 0")

        os.remove("teste1.txt")
        os.remove("teste2.txt")
        os.remove("teste3.txt")

if __name__ == "__main__":
    unittest.main()

doctest.testmod(verbose=True)