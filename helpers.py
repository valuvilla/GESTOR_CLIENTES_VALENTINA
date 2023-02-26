import re
import os
import platform
from colorama import *
from termcolor import colored, cprint
init(autoreset=True)


def limpiar_pantalla() -> None:
    os.system('cls') if platform.system() == "Windows" else os.system('clear')


def leer_texto(min: int = 0, max: int = 100, mensaje: str = None) -> str:
    print(mensaje) if mensaje else None
    while True:
        text = input()
        if len(text) >= min and len(text) <= max:
            return text

    
def dni_valido(dni, lista):
    #comprobar que el dni tiene el formato correcto
    if not re.match('[0-9]{2}[A-Z]$', dni):
        print(Back.RED+f"El formato de DNI: {dni} no es correcto")
        return False
    #comprobar que el dni no está en la lista
    for cliente in lista:
        if cliente.dni == dni:
            print((f"DNI:{dni} utilizado por otro cliente"), ((Back.CYAN+(f"\nCliente Asociado al DNI({cliente.dni}:"),("{cliente.nombre} {cliente.apellido}\n"))))
            return False
    return True
