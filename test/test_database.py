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