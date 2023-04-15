# Programa para uso de listas

nombres = ['alicia', 'beto', 'carlos', 'diana', 100, [2, 5, 1]] #tipos arbitrarios

# longitud = length = tamaño

print(len(nombres))
# son ordenadas
print(nombres)
# pueden ser indexadas por [i]
print(nombres[3])
#son mutables
nombres[3] = 'eva'
print(nombres)
# son dinamicas
nombres.append('fran')
print(nombres)
nombres.remove('beto')
print(nombres)
nombres.pop(1)
print(nombres)
# son iterables
for nombre in nombres:
    print(f'Nombre: {nombre}')