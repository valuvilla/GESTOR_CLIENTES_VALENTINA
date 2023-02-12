


class Cliente:
    def __init__(self, dni, nombre, apellido):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
    
    def __str__(self):
        return f'({self.dni}){self.nombre} {self.apellido}'
    

class Clientes:
    lista = []

    @staticmethod
    def buscar_cliente(dni):
        for cliente in Clientes.lista:
            if cliente.dni == dni:
                return cliente
    
    @staticmethod
    def agregar_cliente(dni, nombre, apellido):
        cliente = Cliente(dni, nombre, apellido)
        Clientes.lista.append(cliente)
        return cliente
    
    @staticmethod
    def modificar_cliente(dni, nombre, apellido):
        for i, cliente in enumerate(Clientes.lista):
            if cliente.dni == dni:
                cliente.lista[i].nombre = nombre
                cliente.lista[i].apellido = apellido
                return Clientes.lista[i]

    @staticmethod
    def eliminar_cliente(dni):
        for i, cliente in enumerate(Clientes.lista):
            if cliente.dni == dni:
                del Clientes.lista[i]
                return cliente