import os
import database as db

def Iniciar():
    os.system('cls')
    print("", "="*25,"\n BIENVENIDO AL GESTOR \n", "="*25, "\n[1] Listar los clientes \n[2] Buscar un cliente \n[3] Agregar un cliente \n[4] Modificar un cliente \n[5] Eliminar un cliente \n[6] Salir", "\n", "="*25)

    opcion= input("Ingrese una opción: ")
    os.system('cls')

    if opcion == "1":
        print("Listar los clientes")
        for cliente in Clientes.lista:
            print(cliente)