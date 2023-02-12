import re
import os
import platform


def limpiar_pantalla():
    os.system('cls') if platform.system() == "Windows" else os.system('clear')

def dni_valido(dni, lista):
    if not re.match('[0-9]{2}[A-Z]$', dni):
        print("DNI incorrecto, debe cumplir el formato.")
        return False
    for cliente in lista:
        if cliente.dni == dni:
            print("DNI utilizado por otro cliente.")
            return False
    return True