import csv
import config


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

    lista = []
    with open(config.DATABASE_PATH, newline='\n') as fichero:
        reader = csv.reader(fichero, delimiter=';')
        for dni, nombre, apellido in reader:
            cliente = Cliente(dni, nombre, apellido)
            lista.append(cliente)

    @staticmethod
    def buscar_cliente(dni):
        for cliente in Clientes.lista:
            if cliente.dni == dni:
                return cliente
    
    @staticmethod
    def agregar_cliente(dni, nombre, apellido):
        cliente = Cliente(dni, nombre, apellido)
        Clientes.lista.append(cliente)
        #Clientes.guardar()
        return cliente
    
    @staticmethod
    def modificar_cliente(dni, nombre, apellido):
        for i, cliente in enumerate(Clientes.lista):
            if cliente.dni == dni:
                Clientes.lista[i].nombre = nombre
                Clientes.lista[i].apellido = apellido
                #Clientes.guardar()
                return Clientes.lista[i]

    @staticmethod
    def eliminar_cliente(dni):
        for i, cliente in enumerate(Clientes.lista):
            if cliente.dni == dni:
                del Clientes.lista[i]
                #Clientes.guardar()
                return cliente

    # @staticmethod
    # def guardar():
    #   with open(config.DATABASE_PATH, 'w', newline='\n') as fichero:
           # writer = csv.writer(fichero, delimiter=';')
           # for cliente in Clientes.lista:
            #    writer.writerow((cliente.dni, cliente.nombre, cliente.apellido))
