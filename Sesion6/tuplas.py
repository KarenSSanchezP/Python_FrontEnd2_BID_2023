lenguajes = ('Python', 'C++', 'PHP', 'Perl', 100, (2, 5, 7))
print(len(lenguajes))
print(lenguajes)
print(lenguajes[0])
# son inmutables
# lenguajes[1] = 'C#'
# son estaticas

#son iterables
for lenguaje in lenguajes:
    print(f'Lenguaje: {lenguaje}')
# estructura de datos de solo lectura