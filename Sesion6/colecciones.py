u1 = {
    'id': 1,
    'usuario': 'alicia',
    'correo': 'alicia@gmail.com',
    'token': 'svydusfefcmxvncvbnxcnvserwrwfudhf',
    'rol': {1: 'admin', 2: 'gerente'},
}

u2 = {
    'id': 2,
    'usuario': 'beto',
    'correo': 'beto@gmail.com',
    'token': 'fyduifyduifhsk nvvnxcvnsudifyieuyr',
    'rol': {3: 'ventas', 4: 'user', 5: 'rrhh'},
}

lista_usuarios = []
lista_usuarios.append(u1)
lista_usuarios.append(u2)

# Una forma de imprimir el correo de beto a partir de la lista
print(lista_usuarios[1]['correo']) 
# Una forma de imprimir el rol admin de alicia
print(lista_usuarios[0]['rol'][1])
# Una forma de imprimir todos los roles de beto haciendo uso de for
for rol in lista_usuarios[1]['rol'].values():
    print(f'Rol de beto: {rol}')
