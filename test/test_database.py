import csv
import copy
import config
import helpers
import unittest
import database as db


class TestDatabase(unittest.TestCase):

    def setUp(self):
        #Antes de cada test
        db.Clientes.lista= [
            db.Cliente('73Y','Valentina','Gonzalez'),
            db.Cliente('85Z','Juan','Perez'),
            db.Cliente('96X','Maria','Gomez'),
        ]

    def test_buscar_cliente(self):
        #Test buscar cliente
        cliente_encontrado = db.Clientes.buscar_cliente('73Y')
        self.assertIsNotNone(cliente_encontrado)
        cliente_no_encontrado = db.Clientes.buscar_cliente('99A')
        self.assertIsNone(cliente_no_encontrado)

    def test_modificar_cliente(self):
        cliente_a_modificar = copy.copy(db.Clientes.buscar_cliente('96X'))
        cliente_modificado = db.Clientes.modificar_cliente('96X','Victoria','Gomez')
        self.assertEqual(cliente_a_modificar.nombre, 'Maria')
        self.assertEqual(cliente_modificado.nombre, 'Victoria')

    def test_agregar_cliente(self):
        #Test agregar cliente
        cliente_agregado = db.Clientes.agregar_cliente('40T','María Del Carmen','Rosales')
        self.assertEqual(len(db.Clientes.lista),4)
        self.assertEqual(cliente_agregado.dni,'40T')
        self.assertEqual(cliente_agregado.nombre,'María Del Carmen')
        self.assertEqual(cliente_agregado.apellido,'Rosales')

    def test_eliminar_cliente(self):
        #Test eliminar cliente
        cliente_eliminado= db.Clientes.eliminar_cliente('85Z')
        cliente_rebuscado= db.Clientes.buscar_cliente('85Z')
        self.assertNotEqual(cliente_eliminado,cliente_rebuscado)
        self.assertIsNone(cliente_rebuscado)

    def test_dni_valido(self):
        #Test dni valido
        self.assertTrue(helpers.dni_valido('00A', db.Clientes.lista))
        self.assertFalse(helpers.dni_valido('232323S', db.Clientes.lista))
        self.assertFalse(helpers.dni_valido('F35', db.Clientes.lista))
        self.assertFalse(helpers.dni_valido('48H', db.Clientes.lista))

    def test_escritura_csv(self):
        db.Clientes.eliminar_cliente('73Y')
        db.Clientes.eliminar_cliente('85Z')
        db.Clientes.modificar_cliente('96X','Victoria','Gomez')

        dni, nombre, apellido= None, None, None
        with open(config.DATABASE_PATH, 'r') as fichero:
            reader = csv.reader(fichero, delimiter=';')
            dni, nombre, apellido = next(reader)

        self.assertEqual(dni,'96X')
        self.assertEqual(nombre,'Victoria')
        self.assertEqual(apellido,'Gomez')




if __name__ == '__main__':
   unittest.main()

