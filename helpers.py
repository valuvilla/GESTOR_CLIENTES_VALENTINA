import re
import os
import platform


def limpiar_pantalla():
    os.system('cls') if platform.system() == "Windows" else os.system('clear')


def leer_text(min=0, max=100, mensaje=None):
    print(mensaje) if mensaje else None
    while True:
        text = input()
        if len(text) >= min or len(text) <= max:
            return text

def dni_valido(dni, lista):
    if not re.match('[0-9]{2}[A-Z]$', dni):
        print("El formato de {dni} no es correct")
        return False
    for cliente in lista:
        if cliente.dni == dni:
            print("DNI:{dni} utilizado por otro cliente.")
            return False
    return True