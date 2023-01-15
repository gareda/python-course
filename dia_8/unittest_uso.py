import unittest
import unittest_prueba


class ProbarCambiaTexto(unittest.TestCase):

    def test_mayusculas(self):
        palabra = "Buen día"
        resultado = unittest_prueba.todo_mayusculas(palabra)
        self.assertEqual(resultado, "BUEN DÍA")


if __name__ == "__main__":
    unittest.main()
