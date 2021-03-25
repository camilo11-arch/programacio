# Variables Globales
i = 1  # Incremento Para El Ciclo

# Ciclo Para Entrar Datos
while i<=3:
    # Imprime La Informacion Para El Estudiante Que Se Requiere
    print('Ingrese las notas para el estudiante ' + str(i))

    # Se Pide que Ingresen Las Notas Pora Los Diferentes Parciales
    Pparcial = float(input('ingrese la nota del primer parcial: '))
    Sparcial = float(input('ingrese la nota del segundo parcial: '))
    Tparcial = float(input('ingrese la nota del tercer parcial: '))
    print()

    # Se Imprime La Información Ingresada
    print('LAS NOTAS INGRSADDAS SON:')
    print('La nota del primer parcial es: ' + str(Pparcial))
    print('La nota del segundo parcial es: ' + str(Sparcial))
    print('La nota del tercer parcial es: ' + str(Tparcial))
    print()

    # Se Crea El Incremetno
    i= i+1
print('GRACIAS POR USAR EL APLICATIVO')
