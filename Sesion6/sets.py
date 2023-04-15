# programa para uso de sets
equipos = {'Barcelona', 'Real Madrid', 'Manchester City', 'Juventus', 'PSG'}
print(len(equipos))
#son desordenados
print(equipos)
#no son indexados
#print(equipos[0])
#son inmutables
#equipos[0] = 'Bayern Munich'
#son dinamicos y no aceptan repetidos
equipos.add('Bayern Munich')
equipos.add('Bayern Munich')
print(equipos)
equipos.discard('PSG')
print(equipos)

#son iterables
for equipo in equipos:
    print(f'Equipo: {equipo}')

