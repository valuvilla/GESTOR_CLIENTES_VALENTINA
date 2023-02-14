import csv
import config
from colorama import *
init(autoreset=True)


class Cliente:
    def __init__(self, dni, nombre, apellido):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
    
    def __str__(self):
        return f'({self.dni}){self.nombre} {self.apellido}'

    def to_dict(self):
        return {'dni': self.dni, 'nombre': self.nombre, 'apellido': self.apellido}
 

class Clientes:
    #Creanos la lista y carrgamos los datos
    lista = []
    

    # Busca un cliente por su DNI
    @staticmethod
    def buscar_cliente(dni: str):
        for cliente in Clientes.lista:  # La lista de clientes se llama lista
            if cliente.dni == dni:  # El cliente tiene un dni, que se compara con el dni que se busca
                r=Back.GREEN+"CLIENTE ENCONTRADO", f"\nNombre: {cliente.nombre} \nApellido: {cliente.apellido} \nDNI: {cliente.dni}"
                return r
        return None
    
    @staticmethod
    def agregar_cliente(dni: int, nombre: str, apellido: str) -> Cliente:
        cliente = Cliente(dni, nombre, apellido)
        Clientes.lista.append(cliente)
        Clientes.guardar()
        return cliente
    
    @staticmethod
    def modificar_cliente(dni: str, nombre: str, apellido: str) -> Cliente:
        for i, cliente in enumerate(Clientes.lista):
            if cliente.dni == dni:
                Clientes.lista[i].nombre = nombre
                Clientes.lista[i].apellido = apellido
                Clientes.guardar()
                return Clientes.lista[i]

    @staticmethod
    def eliminar_cliente(dni: int) -> Cliente:
        for i, cliente in enumerate(Clientes.lista):
            if cliente.dni == dni:
                del Clientes.lista[i]
                Clientes.guardar()
                return cliente
        raise ValueError("El cliente con dni {dni} no existe.")


    @staticmethod
    def guardar():
        with open(config.DATABASE_PATH, 'w', newline='\n') as fichero:
            writer = csv.writer(fichero, delimiter=';')
            for cliente in Clientes.lista:
                writer.writerow((cliente.dni, cliente.nombre, cliente.apellido))
