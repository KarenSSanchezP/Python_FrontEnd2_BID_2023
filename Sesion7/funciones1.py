#Programa para uso de funciones
#(Sin valor de retorno)

def miPrimeraFuncion (nombre):
    print(f"Hola {nombre} bienvenido a Python :D")

miPrimeraFuncion("Alicia")    
miPrimeraFuncion("Alicia")    
miPrimeraFuncion("Alicia")

#Con valor de retorno

def suma(a,b):
    c = a+b
    return c

x = suma(10,5)
print(suma(10,20))