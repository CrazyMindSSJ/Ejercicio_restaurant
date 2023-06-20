#funciones ejercicio restaurant
import numpy
import time
import msvcrt
import os

lista_ruts=[]
lista_nombres=[]
lista_correos=[]
lista_filas=[]
lista_columnas=[]

#arreglo que simboliza al restaurant..
restaurant = numpy.zeros((3,3), int)

def mostrar_menu():
    os.system('cls')
    print("""Bienvenido a restaurant spider-lunch
    Menú
    1. Ver
    2. Reserva
    3. Carta 
    4. Pagar
    5. Cancelar
    6. Salir
    """)
def validar_opcion():
    while True:
        try:
            opc=int(input("Ingrese opcion: "))
            if opc in (1,2,3,4,5,6):
                return opc
            else:
                print("ERROR! Ingrese una opción valida!")
        except:
            print("ERROR! Debe ingresar un número entero")
#funcion para ver el restaurant!
def ver_restaurant():
    for x in range(3):
        print(f"Personas {(x+1)*2}: ",end=" ")
        for y in range(3):
            print(restaurant[x][y], end=" ")
        print()
    print("\nPresione una tecla para continuar...")
    msvcrt.getch()

def validar_rut():
    while True:
        try:
            rut=int(input("Ingrese rut(sin puntos ni digito verificador): "))
            if rut>= 1000000 and rut <= 99999999:
                return
            else:
                print("ERROR! rut debe estar entre 1000000 y 99999999!")
        except:
            print("ERROR! Ingrese un número entero!")

def validar_nombre():
    while True:
        nombre=input("Ingrese su nombre: ")
        if len(nombre.strip()) >=3 and nombre.isalpha:
            return
        else:
            print("ERROR! El nombre debe tener 3 letras minimo")

def validar_correo():
    while True:
        correo=input("Ingrese correo: ")
        if "@" in correo:
            return
        else:
            print("ERROR! Formato de correo incorrecto")

def validar_cantidad():
    while True:
        try:
            cantidad=int(input("Ingrese cantidad de personas: "))
            if cantidad >= 1 and cantidad <=6:
                return
            else:
                print("ERROR! Ingrese cantidad entre 1 y 6")
        except:
            print("ERROR! Ingrese un número entero")

def reserva():
    os.system('cls')
    print("Reserva de mesa")
    rut =  validar_rut()
    nombre = validar_nombre()
    correo = validar_correo()
    ver_restaurant()
    cantidad = validar_cantidad()
    lista_ruts.append(rut)
    lista_correos.append(correo)
    lista_nombres.append(nombre)
