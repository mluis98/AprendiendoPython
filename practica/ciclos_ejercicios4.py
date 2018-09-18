x = []
y = []
for i in range(0, 5):
    numero = input("ingrese un numero")
    if numero % 2 == 0:
        x.append(numero)
    else:
        y.append(numero)

print "pares:" + str(x) 
print "impares" + str(y)