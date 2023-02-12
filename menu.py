import os
import database as db
import helpers

def Iniciar():
    os.system('cls')
    print("", "="*25,"\n BIENVENIDO AL GESTOR \n", "="*25, "\n[1] Listar los clientes \n[2] Buscar un cliente \n[3] Agregar un cliente \n[4] Modificar un cliente \n[5] Eliminar un cliente \n[6] Salir", "\n", "="*25)

    opcion= input("Ingrese una opción: ")
    os.system('cls')

    if opcion == "1":
        print("Listar los clientes\n")
        for cliente in db.Clientes.lista:
            print(cliente)

    elif opcion == "2":
        print("Buscar un cliente\n")
        dni=helpers.leer_text(3, 3, "Ingrese el DNI del cliente: ").upper()
        cliente = db.Clientes.buscar_cliente(dni)
        print(cliente) if cliente else print("El cliente no existe")

    elif opcion == "3":
        print("Agregar un cliente\n")

        dni=None
        while True:
            dni=helpers.leer_text(3, 3, "Ingrese el DNI del cliente: ").upper()
            if db.Clientes.buscar_cliente(dni):
                print("El cliente ya existe")
            else:
                break
