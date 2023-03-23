import math
print("Las funciones son: ")
print("1. Seno")
print("2. Coseno")
print("3. Tangente")
print("4. Exponencial")
print("5. In")

Funcion = int(input("Escriba el numero de la funcion: "))
Numero = int(input("Ingese numero que desea aplicar la funcion: "))

if Funcion == 1:
    print('El numero ingresado es: ',Numero)
    print(f'El resultado es: {math.sin(Numero)}')
if Funcion == 2:
    print('El numero ingresado es: ',Numero)
    print(f'El resultado es: {math.cos(Numero)}')
if Funcion == 3:
    print('El numero ingresado es: ',Numero)
    print(f'El resultado es: {math.tan(Numero)}')
if Funcion == 4:
    print('El numero ingresado es: ',Numero)
    print(f'El resultado es: {math.exp(Numero)}')
if Funcion == 5:
    print('El numero ingresado es: ',Numero)
    print(f'El resultado es: {math.log(Numero)}')

else: 
    if Funcion != 1 or Funcion != 2 or Funcion != 3 or Funcion != 4 or Funcion != 5:
        print("Ese numero de funcion no esta definido")





