# Crear un programa que pida dos numeros y ejecute la multiplicacion rusa

multiplicador = int(input('Digite el multiplicador: '))
multiplicando = int(input('Digite el multiplicando: '))

# Variables auxiliares, para no modificar los datos ingresados por teclado
m, n = multiplicador, multiplicando 
# Equivalente a:
# m = multiplicador
# n = multiplicando 

suma = 0 #inicializamos la suma a cero
while (m >= 1) :
    if (m%2 != 0) :
        suma = suma + n
    else :
        suma = suma
    m = m//2 # doble barra para division entera
    n = n*2

print(f'El resultado de multiplicar {multiplicador} por {multiplicando} es: {suma}')
