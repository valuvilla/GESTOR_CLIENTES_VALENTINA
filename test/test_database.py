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
            db.Cliente('85K','Juan','Perez'),
            db.Cliente('28Z', 'Ana', 'García')
        ]

    def test_buscar_cliente(self):
        cliente_existente = db.Clientes.buscar_cliente('73Y')
        cliente_inexistente = db.Clientes.buscar_cliente('99X')
        self.assertIsNotNone(cliente_existente)
        self.assertIsNone(cliente_inexistente)

    def test_agregar_cliente(self):
        nuevo_cliente = db.Clientes.agregar_cliente('39X', 'María del Carmen', 'Costa')
        self.assertEqual(len(db.Clientes.lista), 4)
        self.assertEqual(nuevo_cliente.dni, '39X')
        self.assertEqual(nuevo_cliente.nombre, 'María del Carmen')
        self.assertEqual(nuevo_cliente.apellido, 'Costa')

    def test_modificar_cliente(self):
        cliente_a_modificar = copy.copy(db.Clientes.buscar_cliente('28Z'))
        cliente_modificado = db.Clientes.modificar_cliente('28Z', 'Mariana', 'García')
        self.assertEqual(cliente_a_modificar.nombre, 'Ana')
        self.assertEqual(cliente_modificado.nombre, 'Mariana')

    def test_eliminar_cliente(self):
        cliente_a_eliminar = copy.copy(db.Clientes.buscar_cliente('85K'))
        cliente_eliminado = db.Clientes.eliminar_cliente('85K')
        self.assertEqual(cliente_a_eliminar.dni, '85K')
        self.assertIsNone(cliente_eliminado)

    def test_dni_valido(self):
        self.assertTrue(helpers.dni_valido('00A', db.Clientes.lista))
        self.assertFalse(helpers.dni_valido('232323S', db.Clientes.lista))
        self.assertFalse(helpers.dni_valido('F35', db.Clientes.lista))
        self.assertFalse(helpers.dni_valido('48H', db.Clientes.lista))


