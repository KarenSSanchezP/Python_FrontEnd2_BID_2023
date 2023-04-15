#pedir la hora

hora = input('Digite la hora: ')
print('la hora digitada es: '+hora)
print('el tipo de hora es: ', type(hora))

#conversion de tipos (str a int)
hora = int(hora)

if hora>12:
    print('Buenas tardes')
    print('Pase adelante')
    if hora>=18:
        print('Buenas noches tambien')
else:
    print('Buenos dias')