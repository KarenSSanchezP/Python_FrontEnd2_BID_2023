# Programa para uso de diccionarios
# Los diccionarios nos permiten "indexar" los valores no por posiciones, 
# sino por "nombres" que es a lo que llamamos llaves
user = {
    # llave   :   valor
    'usuario': 'alicia',
    'correo': 'alicia@gmail.com',
    'token': 'svydusfefcmxvncvbnxcnvserwrwfudhf',
}
# Acceso por llaves
print('Usuario:', user['usuario'])
print('Correo:', user['correo'])
print('Token:', user['token'])

# Son mutables, es decir, pueden ser modificados despues de ser declarados
user['usuario'] = 'alicia123' # cambiamos el valor de la llave 'usuario'
print('Usuario:', user['usuario'])

# Son dinamicos
user['telefono'] = '123456789' # incluimos una nueva llave
print(user)
user.pop('token') # eliminamos la llave 'token'

for valor in user.values(): # imprimimos solo los valores de las llaves
    print(f'Valor: {valor}')

for llave in user.keys(): # imprimimos los nombres de las llaves
    print(f'llave: {llave}')

for k, v in user.items(): # imprimimos las llaves con su valor correspondiente
    print(f'llave: {k}, valor: {v}')
