import os
import database as db
import helpers

def Iniciar():
    helpers.limpiar_pantalla()
    print("", "="*25,"\n BIENVENIDO AL GESTOR \n", "="*25, "\n[1] Listar los clientes \n[2] Buscar un cliente \n[3] Agregar un cliente \n[4] Modificar un cliente \n[5] Eliminar un cliente \n[6] Salir", "\n", "="*25)

    opcion= input("Ingrese una opción: ")
    helpers.limpiar_pantalla()

    if opcion == "1":
        #Listar los clientes
        print("Listar los clientes.....\n")
        for cliente in db.Clientes.lista:
            print(cliente)

    elif opcion == "2":
        print("Buscar un cliente....\n")
        dni=helpers.leer_text(3, 3, "Ingrese el DNI del cliente(2 int y 1 char): ").upper()
        cliente = db.Clientes.buscar_cliente(dni)
        print(cliente) if cliente else print("El cliente no existe")
    
    
    elif opcion == "3":
        print("Agregar un cliente.....\n")

        dni=None

        while True:
        # Preguntar el DNI del cliente
            dni=helpers.leer_text(3, 3, "Ingrese el DNI del cliente: ").upper()
        # Validar el DNI
            if helpers.dni_valido(dni, db.Clientes.lista):
               break 

        # Preguntar el nombre  y apellido  del cliente
        nombre= helpers.leer_text(2, 30, "Ingrese el nombre del cliente(2 a 30 chars): ").capitalize()
        apellido= helpers.leer_text(2, 30, "Ingrese el apellido del cliente(2 a 30 chars): ").capitalize()
        #
        db.Clientes.agregar_cliente(dni, nombre, apellido)
        print("Cliente agregado con éxito")

    elif opcion == "4":
        print("Modificar un cliente.....\n")
        # Preguntar el DNI del cliente
        dni=helpers.leer_text(3, 3, "Ingrese el DNI del cliente(2 int y 1 char): ").upper()
        # 
        cliente = db.Clientes.buscar_cliente(dni)
        if cliente:
            nombre=helpers.leer_texto(
                2, 30, f"Ingrese el nombre del cliente (de 2 a 30 chars): ({cliente.nombre}): ").capitalize()
            apellido=helpers.leer_texto(
                2, 30, f"Ingrese el apellido del cliente (de 2 a 30 chars): ({cliente.apellido}): ").capitalize()
            db.Clientes.modificar_cliente(cliente.dni, nombre, apellido)
            print("Cliente (nombre: {nombre}, apellido: {apellido}, dni: {cliente.dni}) modificado con éxito")
        else:
            print("El cliente con DNI: {dni} no existe")

    elif opcion == "5":
        print("Eliminar un cliente.....\n")
        dni=helpers.leer_text(3, 3, "Ingrese el DNI del cliente(2 int y 1 char): ").upper()
        print("El cliente (nombre: {nombre}, apellido: {apellido}, dni: {Cliente.dni}) se ha borrado con éxito") if db.Clientes.eliminar_cliente(
            dni) else print("El cliente (nombre: {nombre}, apellido: {apellido}, dni: {Cliente.dni}) no existe")

    elif opcion == "6":
        print("Salir.....\n")
        os._exit(0)

    input("\nPresiona ENTER para continuar...")

Iniciar()