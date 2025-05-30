import unittest
from calculadora_gauderia import calcular

class TestCalculadoraGauderia(unittest.TestCase):

    def test_soma_sem_overflow(self):
        self.assertEqual(calcular("00000001", "00000001", "+"), "00000010")
        self.assertEqual(calcular("00000010", "00000100", "+"), "00000110")

    def test_soma_com_overflow(self):
        with self.assertRaises(Exception) as cm:
            calcular("01111111", "00000001", "+")
        self.assertEqual(str(cm.exception), "overflow")

    def test_subtracao_sem_overflow(self):
        self.assertEqual(calcular("00000101", "00000001", "-"), "00000100")
        self.assertEqual(calcular("00000010", "00000010", "-"), "00000000")

    def test_subtracao_com_overflow(self):
        with self.assertRaises(Exception) as cm:
            calcular("10000000", "00000001", "-")
        self.assertEqual(str(cm.exception), "overflow")

    def test_multiplicacao_sem_overflow(self):
        self.assertEqual(calcular("00000010", "00000011", "x"), "00000110")  # 2 x 3 = 6
        self.assertEqual(calcular("11111111", "00000001", "x"), "11111111")  # -1 x 1 = -1

    def test_multiplicacao_com_overflow(self):
        with self.assertRaises(Exception) as cm:
            calcular("01111111", "00000010", "x")  # 127 x 2 = 254 > 127
        self.assertEqual(str(cm.exception), "overflow")

    def test_valor_invalido(self):
        with self.assertRaises(Exception) as cm:
            calcular("0000000A", "00000001", "+")
        self.assertEqual(str(cm.exception), "valor invalido")

        with self.assertRaises(Exception) as cm:
            calcular("00000001", "00002", "+")
        self.assertEqual(str(cm.exception), "tamanho da entrada invalido")

        with self.assertRaises(Exception) as cm:
            calcular("00000001", "00000001", "*")
        self.assertEqual(str(cm.exception), "valor invalido")

    def test_negativos(self):
        self.assertEqual(calcular("11111111", "00000001", "+"), "00000000")  # -1 + 1 = 0
        self.assertEqual(calcular("11111110", "00000010", "+"), "00000000")  # -2 + 2 = 0
        self.assertEqual(calcular("00000001", "11111111", "+"), "00000000")  # 1 + (-1) = 0

if __name__ == "__main__":
    unittest.main()
