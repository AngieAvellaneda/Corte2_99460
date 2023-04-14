def main():
    f = open('organization_data.csv','rt')
    lista = f.readlines()
    matriz = []
    f.seek(0)
    
    for i in range(len(lista)):
        matriz.append([])
        valor = f.readline().rstrip('\n').split(',')
        for j in range(len(valor)):
            matriz[i].append(valor[j])
   
    paises = sorted(matriz,key = lambda x:x[4])
   
main()
            

