import csv
import copy
import config
import helpers
import unittest
import database as db


class TestDatabase(unittest.TestCase):

    def setUp(self):
        #Antes de cada test
        db.Clientes.lista_clientes= [
            db.Cliente('73Y','Valentina','Gonzalez'),
            db.Cliente('85Z','Juan','Perez'),
            db.Cliente('96X','Maria','Gomez'),
            db.Cliente('12W','Pedro','Gonzalez'),
        ]

    def test_buscar_cliente(self):
        #Test buscar cliente
        cliente_encontrado = db.Clientes.buscar_cliente('73Y')
        self.assertIsNotNone(cliente_encontrado)
        cliente_no_encontrado = db.Clientes.buscar_cliente('99A')
        self.assertIsNone(cliente_no_encontrado)

    def test_agregar_cliente(self):
        #Test agregar cliente
        cliente_agregado = db.Clientes.agregar_cliente('40T','María Del Carmen','Rosales')
        self.assertEqual(len(db.Clientes.lista_clientes),5)
        self.assertEqual(cliente_agregado.dni,'40T')
        self.assertEqual(cliente_agregado.nombre,'María Del Carmen')
        self.assertEqual(cliente_agregado.apellido,'Rosales')

    def test_modificar_cliente(self):
        #Test modificar cliente
        cliente_sin_modificar = db.Clientes.buscar_cliente('73Y','Valentina','Gonzalez')
        cliente_modificado= db.Clientes.modificar_cliente('73Y','Valentina','Villalobos')
        self.assertEqual(cliente_sin_modificar.apellido,'Gonzalez')
        self.assertEqual(cliente_modificado.apellido,'Villalobos')

    def test_eliminar_cliente(self):
        #Test eliminar cliente
        cliente_eliminado= db.Clientes.eliminar_cliente('85Z')
        cliente_rebuscado= db.Clientes.buscar_cliente('85Z')
        self.assertNotEqual(cliente_eliminado,cliente_rebuscado)



if __name__ == '__main__':
    unittest.main()

