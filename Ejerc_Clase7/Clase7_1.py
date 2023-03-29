Horario = [['Taller fisica mecanica', 'Cultura ecologica', 'Democracia', 'Calculo integral', 'Fisica mecanica', 'Circuitos DC', 'Programacion'], ['Lunes','Virtual','Lunes','Martes y jueves','Martes y jueves','Martes y jueves','Martes y jueves'],['1 p.m','Hora no especifica','3 p.m','7 a.m','9 a.m','11 a.m','1 p.m'],['306DB','Virtual','304DB','406DB','405DB','306DB','303GO'],['Julian Ortiz','Catelina Gonzales','Catelina Gonzales','Jairo Lalinde','Hernan Pineda','Hernan Pineda','David Torres']]
Palabra = input('Que materia esta buscando: ')

for i in range(len(Horario[0])):
    if Palabra.lower() ==  Horario[0][i].lower():
        Columna = i
        break

print(f'El horario es ')

for j in range(len(Horario)):
  print(Horario[j][Columna])

