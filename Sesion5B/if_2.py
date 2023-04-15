#pedir la hora
hora = int(input('Digite la hora: '))

if hora>=1 and hora<12:
    print('Buenos dias')
elif hora>=12 and hora<18:
    print('Buenas tardes')
elif hora>=18 and hora<=24:
    print('Buenas noches')
else:
    print('hora no valida')