# Se Pide Que Ingresen Información
n = int(input('Ingrese la cantidad de trabajadores: '))                                  # Cantidad Trabajadores
k = int(input('Ingresen la cantidad de horas que tardan en realizar la actividad: '))    # Tiempo Que Tardan En Realizar La Activida
KNew = int(input('Ingrese las horas que desee que tarden en realizar la actividad: '))   # Tiempo Que Se Desea Que Se Tarden En Realizar La Actividad

# Se Aplica La Regla De Tres Para Hallar El Tiempo
x = (KNew*n)/k  # Cantidad de trabajadores Requeridos
print()

# Se Imprime La Respuesta De Los Trabajadores requeridos
print('La cantidad de trabajadores que se requieren para realizar la actividad en ' + str(KNew) + str(' horas es: ') + str(x))
