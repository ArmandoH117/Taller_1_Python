import os
import time


def celsius_a_fahrenheit(celcius):
    return(celcius * 9/5 ) + 32

def fahrenheit_a_celsius(fahrenheit):
    return(fahrenheit - 32) * 5/9

flag = True
while flag:
    os.system("cls")
    print("--Bienvenidos a este convertidor")
    print("--MENU")
    print("1) Celcius a fahrenhei")
    print("2) Fahrenhei a Celcius")
    print("0) Salir")
    print("---------------------------------")
    opc = input("Ingrese una opcion: ")
    os.system("cls")

    match opc:
        case '1':
            grados = float(input("Ingrese en Celcius: "))
            resultado = celsius_a_fahrenheit(grados)
            print(f"{grados} Celcius equivalen a {resultado}")
            os.system("pause")
        case '2':
            grados = float(input("Ingrese en fahrenheit: "))
            resultado = fahrenheit_a_celsius(grados)
            print(f"{grados} fahrenheit equivalen a {resultado} Celcius")
            os.system("pause")
        case '0':
            flag = False
            print("Hasta pronto....")
            time.sleep(3)
            os.system("cls")

    

