#programa para operadores aritmeticos

a=10
b=3

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)
print(a**b)

#precedencia
#()
# **
# * / // %
# + -
# igual jerarquia, asociatividad por izquierda
print('aplicando precedencia', 4+5*2**3) #44 
print('aplicando precedencia', (4+5)*2**3) #72
print('aplicando precedencia', 10/5*2) #4
