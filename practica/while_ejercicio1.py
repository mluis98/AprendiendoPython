pares = []
while True:
    numero = input("ingrese un mumero")
    if numero == 0:
        break
    if ((numero % 2 == 0) and (numero not in pares)):
        pares.append(numero)
    else:
        print str(numero) + " no es par"
print "pares" + str(pares)

