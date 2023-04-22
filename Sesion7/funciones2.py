#Programa de paso de por valor de refencia
#Por copia
x = 2
def modificarVariable(y):
    y += 5
    return y
z = modificarVariable(x)
print(z)
print(x)

#Por direccion

v = [2,6,4]
def modificarVector(w):
    w.append(0)
    return w
t = modificarVector(v)
print(t)
print(v)