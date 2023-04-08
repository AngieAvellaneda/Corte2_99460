def main():
    f = open('Alimentos.txt','rt')
    lista = f.readlines()
    matriz = []
    f.seek(0)
    suma = 0
    for i in range(len(lista)):
        matriz.append([])
        valor = f.readline().rstrip('\n').split(',')
        for j in range(len(valor)):
            matriz[i].append(valor[j])
    Nombre = ''
    while Nombre != 'salir':
        Nombre = input('Ingrese el nombre del producto: ').lower()
        valor = float(input('Ingrese su respectivo valor: '))
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if Nombre in matriz[i][j].lower():
                    IVA = float(matriz[i][2])
                    break
        IVA_discriminado = valor*IVA
        valor_bruto = valor - IVA_discriminado
        print(f'El valor bruto del producto es {valor_bruto} y su respectivo IVA discriminado es {IVA_discriminado}') 
main()

