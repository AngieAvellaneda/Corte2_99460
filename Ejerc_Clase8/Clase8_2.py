n=int(input('Ingrese valor de n: '))
p=int(input('Ingrese valor de p: '))
def ecuacion(n,p,resu):
  if n!=0:
     R=n*p
     resultado = R + resu
     print(resultado)
     ecuacion(n-1,p,resultado)
ecuacion(n,p,0)