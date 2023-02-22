import csv
import config
from colorama import *
import pandas as pd
init(autoreset=True)

class Cliente:
    def __init__(self, dni, nombre, apellido):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f"({self.dni}) {self.nombre} {self.apellido}"

    def to_dict(self):
        return {'dni': self.dni, 'nombre': self.nombre, 'apellido': self.apellido}

class Clientes:
    #Creanos la lista y carrgamos los datos
    lista=[]
    with open(config.DATABASE_PATH, newline='\n') as fichero:
        reader = csv.reader(fichero, delimiter=';')
        for dni, nombre, apellido in reader:
            cliente = Cliente(dni, nombre, apellido)
            lista.append(cliente)

    # Busca un cliente por su DNI
    @staticmethod
    def buscar_cliente(dni):
        for cliente in Clientes.lista: #iteramos en la lista de clientes y buscamos el dni que le pasamos por parametro
            if cliente.dni == dni: #si el dni del cliente que estamos iterando es igual al que le pasamos por parametro
                print(Back.GREEN+"\nCliente encontrado") #imprimimos que lo encontramos
                return  f"Nombre: {cliente.nombre} \nApellido: {cliente.apellido} \nDNI: {cliente.dni}" #y retornamos la informacion del cliente
        
    @staticmethod
    def agregar_cliente(dni, nombre, apellido):
        # Crear el objeto cliente.
        cliente = Cliente(dni, nombre, apellido)
        # Agregar el cliente a la lista.
        Clientes.lista.append(cliente)
        # Guardar en el archivo.
        Clientes.guardar()
        # Devolver el cliente.
        return cliente
    
    @staticmethod
    def modificar_cliente(dni, nombre, apellido):
        for indice, cliente in enumerate(Clientes.lista):
            if cliente.dni == dni:
                # Modificar el cliente de la lista
                Clientes.lista[indice].nombre = nombre
                Clientes.lista[indice].apellido = apellido
                # Guardar los cambios en el archivo
                Clientes.guardar()
                # Devolver el cliente modificado
                return Clientes.lista[indice]

    @staticmethod
    def eliminar_cliente(dni):
        # Recorrer la lista de clientes
        for indice, cliente in enumerate(Clientes.lista):
            # Si el dni del cliente coincide con el dni pasado por parámetro
            if cliente.dni == dni:
                # Eliminar el cliente de la lista
                del Clientes.lista[indice]
                # Guardar los cambios en el archivo
                Clientes.guardar()
                # Devolver el cliente eliminado
                return cliente


    @staticmethod
    def guardar():
        with open(config.DATABASE_PATH, 'w', newline='\n') as fichero:
            writer = csv.writer(fichero, delimiter=';')
            for cliente in Clientes.lista:
                writer.writerow((cliente.dni, cliente.nombre, cliente.apellido))
