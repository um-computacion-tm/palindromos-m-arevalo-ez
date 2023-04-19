import unittest
from palindromos import palindromo
class TestPalindromos(unittest.TestCase):

    def test_Neuquen(self):
        resultado = palindromo("neuquen")
        self.assertEqual(resultado, "YES")

    def test_Anna(self):
        resultado = palindromo("anna")
        self.assertEqual(resultado, "YES")

    def test_Mendoza(self):
        resultado = palindromo("mendoza")
        self.assertEqual(resultado, "NO")

    def test_Otto(self):
        resultado = palindromo("otto")
        self.assertEqual(resultado, "YES")

    def test_5(self):
        resultado = palindromo("anita lava la tina")
        self.assertEqual(resultado, "YES")

    def test_6(self):
        resultado = palindromo("mañana es lunes")
        self.assertEqual(resultado, "NO")

    def test_7(self):
        resultado = palindromo("luz azul")
        self.assertEqual(resultado, "YES")

if __name__ == '__main__':
    unittest.main()