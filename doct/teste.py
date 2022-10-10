import sys



import aula as mq
import unittest
from datetime import date
from unittest.mock import Mock
def setUpModule():
    print('\nExecutando SetUpModule')

def tearDownModule():
    print('\nExecutando tearDownModule')

class TestModuloQualidade(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('\nExecutando setUpClass')
    @classmethod
    def tearDownClass(cls):
        print('\nexecutando tearDownClass')
    def setUp(self):
        print('\nExecutando setUpClass')
    def tearDown(self):
        print('\nExecutando tearDownMethod')
    def test_case_funcao_2(self):
        print('Teste de alerta ponto de fulgor etanol verdadeiro')
        self.assertTrue(mq.funcao2('bola',10,{"item1": 1, "item2": 3, "item3": 6}),{'item1': 1, 'item2': 3, 'item3': 6, 'bola': 10})
if __name__ == '__main__':
    unittest.main(verbosity=2)

