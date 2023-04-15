n = int(input('Digite un numero'))

f = n

for i in range(1, n):
    f = f*i

# i=1
# while(i<n)
#   f *= i
#   i+=1

print(f'El factorial de {n} es: {f}')

