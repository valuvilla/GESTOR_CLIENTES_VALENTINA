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
            db.Cliente('28Z', 'Ana', 'García')
        ]

    def test_buscar_cliente(self):
        cliente_existente=db.Clientes.buscar_cliente('73Y')
        cliente_inexistente=db.Clientes.buscar_cliente('00A')
        self.assertIsNotNone(cliente_existente)
        self.assertIsNone(cliente_inexistente)
        # assercion, excepcion, mensaje

    def test_agregar_cliente(self):
        #Test agregar cliente
        cliente_agregado = db.Clientes.agregar_cliente('40T','María Del Carmen','Rosales')
        self.assertEqual(len(db.Clientes.lista),4)
        self.assertEqual(cliente_agregado.dni,'40T')
        self.assertEqual(cliente_agregado.nombre,'María Del Carmen')
        self.assertEqual(cliente_agregado.apellido,'Rosales')

    def test_modificar_cliente(self):
        cliente_a_modificar = copy.copy(db.Clientes.buscar_cliente('28Z'))
        cliente_modificado = db.Clientes.modificar_cliente('28Z', 'Mariana', 'García')
        self.assertEqual(cliente_a_modificar.nombre, 'Ana')
        self.assertEqual(cliente_modificado.nombre, 'Mariana')


    def test_eliminar_cliente(self):
        #Test eliminar cliente
        cliente_borrado = db.Clientes.eliminar_cliente('85Z')
        cliente_rebuscado = db.Clientes.buscar_cliente('85Z')
        self.assertEqual(cliente_borrado.dni,'85Z')
        self.assertIsNone(cliente_rebuscado)

    def test_dni_valido(self):
        #Test dni valido
        self.assertTrue(helpers.dni_valido('00A', db.Clientes.lista))
        self.assertFalse(helpers.dni_valido('232323S', db.Clientes.lista))
        self.assertFalse(helpers.dni_valido('F35', db.Clientes.lista))
        self.assertFalse(helpers.dni_valido('73Y', db.Clientes.lista))

    def test_escritura_csv(self):
        #Test escritura csv
        db.Clientes.eliminar_cliente('73Y')
        db.Clientes.eliminar_cliente('85Z')
        db.Clientes.modificar_cliente('28Z', 'Mariana', 'García')


        dni, nombre, apellido = None, None, None
        with open(config.DATABASE_PATH, 'r') as fichero:
            reader: csv.reader = csv.reader(fichero, delimiter=';')
            dni, nombre, apellido = next(reader)
            
        self.assertEqual(dni, '28Z')
        self.assertEqual(nombre, 'Mariana')
        self.assertEqual(apellido, 'García')
        