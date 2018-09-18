listado = []

for x in range(0, 5):
    nombre = raw_input("ingrese un nombre")
    if nombre in listado:
        print nombre + " ya es su amigo"
    else:
        listado.append(nombre) 

print "sus amigos son:" + str(listado)
