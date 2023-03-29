import random as r

Numeros = []
for i in range(10):
    Numeros.append(r.randint(1,50))
print(Numeros)

def Mayor(Numeros):
    Numeros.sort()
    print(f'El numero mayor es: {Numeros[-1]}')
Mayor(Numeros)
print('Los numeros primos son:')

def Primos(Numeros):
    for i in range(len(Numeros)):
            Primo = True
            for j in range(2,Numeros[i]):
                if Numeros[i]%j==0:
                    Primo = False
                    
            if Primo != False:
                print(Numeros[i],end=',')
Primos(Numeros)