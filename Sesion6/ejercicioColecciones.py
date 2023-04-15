#Crear un programa que capture los datos de N empleados:
# - nombre
# - cargo
# - sueldo
#Crear el siguiente menu
#    1. Agregar empleado
#    2. Imprimir lista
#    3. Salir
#para cada empleado construir un diccionario que se ira 
#agregando a una lista que será impresa con la opción 2 del menu

lista_empleados = [] #Inicializamos la lista con cero elementos

opcion = int(input(f'Escoja una opcion: \n'
                '1. Agregar empleado \n'
                '2. Imprimir lista \n'
                '3. Salir \n')) 

while(opcion != 3) :
    if (opcion == 1):
        print(f'\nAgregando empleado')
        empleado = {
        'nombre': input(f'Ingrese el nombre: '),
        'cargo' : input(f'Ingrese el cargo: '),
        'sueldo': input(f'Ingrese el sueldo: '),
        }
        lista_empleados.append(empleado)
    elif (opcion == 2) :
        print(f'\nImprimiendo lista: \n {lista_empleados} \n')
        
    opcion = int(input(f'\nEscoja una opcion: \n'
                '1. Agregar empleado \n'
                '2. Imprimir lista \n'
                '3. Salir \n'))
    
