

print("--Bienvenido a esta calculadora")
print("--Menu: ")
print("1) Suma ")
print("2) Resta ")
print("3) Multiplicacion ")
print("4) Division ")
print("--------------")
opc = input("Ingrese la opcion: ")

match(opc):
    case '1':
        a = float(input('Ingrese el primer numero: '))
        b = float(input('Ingrese el segundo numero: '))
        sum = a + b
        print(f"{a} + {b} = {sum}")
    case '2':
        a = float(input('Ingrese el primer numero: '))
        b = float(input('Ingrese el segundo numero: '))
        resta = a - b
        print(f"{a} - {b} = {resta}")
    case '3':
        a = float(input('Ingrese el primer numero: '))
        b = float(input('Ingrese el segundo numero: '))
        mult = a * b
        print(f"{a} x {b} = {mult}")
    case '4':
        a = float(input('Ingrese el primer numero: '))
        b = float(input('Ingrese el segundo numero: '))
        if a == 0 or b == 0:
            print("No se puede dividir entre cero")
        else:
            div = a / b
            print(f"{a} / {b} = {div}")




        



