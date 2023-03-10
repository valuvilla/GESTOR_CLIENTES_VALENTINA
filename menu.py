import os
import re
import database as db
import helpers
from colorama import *
from termcolor import colored, cprint
init(autoreset=True)

def iniciar():
    while True:
        helpers.limpiar_pantalla()

        lineas=(Fore.GREEN+"=="*18)
        print(lineas)
        print(colored("  BIENVENIDO AL GESTOR DE CLIENTES  ", 'white', attrs=['bold'], on_color='on_green'))
        print( lineas)
        print(colored(Fore.LIGHTGREEN_EX+"[1]"),"Listar clientes")
        print(colored(Fore.LIGHTGREEN_EX+"[2]"),"Buscar un cliente")
        print(colored(Fore.LIGHTGREEN_EX+"[3]"),"Añadir un cliente")
        print(colored(Fore.LIGHTGREEN_EX+"[4]"),"Modificar un cliente")
        print(colored(Fore.LIGHTGREEN_EX+"[5]"),"Borrar un cliente")
        print(colored(Fore.LIGHTGREEN_EX+"[6]"),"Cerrar el Gestor")# CERRAR EL MANAGER
        print(lineas)

        opcion = input(colored(Fore.LIGHTGREEN_EX+"> "))
        helpers.limpiar_pantalla()

        if opcion == '1':
            print(Back.LIGHTGREEN_EX+"Listando los clientes...\n")
            for cliente in db.Clientes.lista:
                print(cliente)

        elif opcion == '2':
            print(Back.LIGHTGREEN_EX+"Buscando un cliente...\n")
            dni = None
            while True:
                dni = helpers.leer_texto(3, 3, "DNI (2 int y 1 char)").upper()
                if re.match('[0-9]{2}[A-Z]$', dni):
                    break
            cliente = db.Clientes.buscar_cliente(dni)
            print(cliente) if cliente else print(Fore.RED+f"Cliente de DNI: {dni} no encontrado.")

        elif opcion == '3':
            print(Back.LIGHTGREEN_EX+"Añadiendo un cliente...\n")

            dni = None
            while True:
                dni = helpers.leer_texto(3, 3, "DNI (2 int y 1 char)").upper()
                if helpers.dni_valido(dni, db.Clientes.lista):
                    break

            nombre = helpers.leer_texto(2, 30, "Nombre (de 2 a 30 chars)").capitalize()
            apellido = helpers.leer_texto(2, 30, "Apellido (de 2 a 30 chars)").capitalize()
            db.Clientes.agregar_cliente(dni, nombre, apellido)
            print((Back.GREEN+"\nCliente añadido correctamente"), (Fore.GREEN+'\nDatos del cliente:'))
            print(f"DNI: {dni} \nNombre: {nombre} \nApellido: {apellido}")

        elif opcion == '4':
            print(Back.LIGHTGREEN_EX+"Modificando un cliente...\n")
            dni = helpers.leer_texto(3, 3, "DNI (2 int y 1 char)").upper()
            cliente = db.Clientes.buscar_cliente(dni)
            if cliente:
                nombre = helpers.leer_texto(
                    2, 30, f"Nombre antiguo: {nombre} \nNombre actual (de 2 a 30 chars)").capitalize()
                apellido = helpers.leer_texto(
                    2, 30, f"Apellido Antiguo: {apellido} \nApellido actual (de 2 a 30 chars)").capitalize()
                db.Clientes.modificar_cliente(dni, nombre, apellido)
                print(Back.GREEN+"Cliente modificado correctamente.")
                print(f"Nombre: {nombre} \nApellido: {apellido} \nDNI: {dni}")
            else:
                print(Fore.RED+f"Cliente de DNI: {cliente.dni} no encontrado.")

        elif opcion == '5':
            print(Back.LIGHTGREEN_EX+"Borrando un cliente...\n")
            dni = helpers.leer_texto(3, 3, "DNI (2 int y 1 char)").upper()
            print(f"Cliente de DNI: {dni} borrado correctamente.") if db.Clientes.eliminar_cliente(
                dni) else print(Fore.RED+f"Cliente de DNI: {dni} no encontrado.")

        elif opcion == '6':
            print(Back.MAGENTA+"SALIENDO\n")
            break

        input("\nPresiona ENTER para continuar...")

