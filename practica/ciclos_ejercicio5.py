amigos = []

while True:
    nombre = raw_input("Ingrese un nuevo amigo: ")

    if nombre == "end":
        break
    else:
        if nombre in amigos:
            print nombre + " ya es tu amigo."
        else:
            amigos.append(nombre)

print "Tus amigos: " + str(amigos)