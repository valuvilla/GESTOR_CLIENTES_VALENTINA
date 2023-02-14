import re
import os
import platform


def limpiar_pantalla() -> None:
    os.system('cls') if platform.system() == "Windows" else os.system('clear')


def leer_texto(min: int = 0, max: int = 100, mensaje: str = None) -> str:
    print(mensaje) if mensaje else None
    while True:
        text = input()
        if len(text) >= min and len(text) <= max:
            print("El texto es válido")
            return text
        print("El texto es inválido")

    
def dni_valido(dni, lista):
    #comprobar que el dni tiene el formato correcto
    if not re.match('[0-9]{2}[A-Z]$', dni):
        print("El formato de DNI: {dni} no es correcto")
        return False
    #comprobar que el dni no está en la lista
    for cliente in lista:
        if cliente.dni == dni:
            print("DNI:{dni} utilizado por otro cliente.")
            return False
    return True