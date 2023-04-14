def main():
    f = open('organization_data.csv','rt')
    paises = []
    lista = f.readlines()
    f.seek(0)
    for i in range(len(lista)):
        paises.append([])
        valores = f.readline().rstrip('\n').split(',')
        for j in range(len(valores)):
            paises[i].append(valores[j])

    paises_ordenados = [paises[0]]
    paises = sorted(paises, key=lambda x:x[4])

    lista_paises = []
    for i in range(243):
        for j in range(len(paises)):
            if j+1 != 10000:
                if paises[j][4] == paises[j+1][4]:
                    pass
                elif paises[j][4] == "Country":
                    pass
                else:
                    lista_paises.append(paises[j][4])
            else:
                lista_paises.append(paises[j][4])
                break

    for i in range(243):
        paises_ordenados.append([])
        for j in range(len(paises)):
                if lista_paises[i] == paises[j][4]:
                    paises_ordenados[i+1].append(paises[j])


    buscar = int(input("Indice del paise de busqueda: "))
    print(f"\nPais:{paises_ordenados[buscar][0][4]}")
    print("\nEmpresa con mayor # de empleados: ")

    empresas = sorted(paises_ordenados[buscar], key= lambda x: int(x[8]))
    print(f"- {paises_ordenados[0][2]}:{empresas[-1][2]}")
    print(f"- {paises_ordenados[0][3]}:{empresas[-1][3]}")
    print(f"- {paises_ordenados[0][5]}:{empresas[-1][5]}")
    print(f"- {paises_ordenados[0][6]}:{empresas[-1][6]}")
    print(f"- {paises_ordenados[0][7]}:{empresas[-1][7]}")
    print(f"- {paises_ordenados[0][8]}:{empresas[-1][8]}")
    

    print("\nEmpresa con menor # de empleados: ")
    print(f"- {paises_ordenados[0][2]}:{empresas[0][2]}")
    print(f"- {paises_ordenados[0][3]}:{empresas[0][3]}")
    print(f"- {paises_ordenados[0][5]}:{empresas[0][5]}")
    print(f"- {paises_ordenados[0][6]}:{empresas[0][6]}")
    print(f"- {paises_ordenados[0][7]}:{empresas[0][7]}")
    print(f"- {paises_ordenados[0][8]}:{empresas[0][8]}")

    empleados = []
    for i in range(len(empresas)):
        empleados.append(int(empresas[i][8]))

    Promedio = sum(empleados) / len(empresas)
    print(f"\nPromedio empreados {format(Promedio, '.2f')}")
    print(f"Cantidad de empresas: {len(empresas)}")


main()
