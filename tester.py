import unittest
import requests


class Test_calculadora(unittest.TestCase):
    def teste(self):
        r = requests.get('http://127.0.0.1:5005')
        if r.status_code == 404:
            self.fail("Página não definida")
        else:
            self.assertEqual(r.status_code, 200)




if __name__ == "__name__":
    unittest.main()