


class Cliente:
    def __init__(self, dni, nombre, apellido, direccion, telefono, email):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
    
    def __str__(self):
        return f'({self.dni}){self.nombre} {self.apellido}'
    

class Clientes:
    lista_clientes = []

    @staticmethod
    def buscar_cliente(dni):
        for cliente in Clientes.lista_clientes:
            if cliente.dni == dni:
                return cliente
    
    @staticmethod
    def agregar_cliente(dni, nombre, apellido):
        cliente = Cliente(dni, nombre, apellido)
        Clientes.lista_clientes.append(cliente)
        return cliente
    
    @staticmethod
    def modificar_cliente(dni, nombre, apellido):
        for i, cliente in enumerate(Clientes.lista_clientes):
            if cliente.dni == dni:
                cliente.lista_clientes[i].nombre = nombre
                cliente.lista_clientes[i].apellido = apellido
                return Clientes.lista_clientes[i]

    @staticmethod
    def eliminar_cliente(dni):
        for i, cliente in enumerate(Clientes.lista_clientes):
            if cliente.dni == dni:
                del Clientes.lista_clientes[i]
                return cliente