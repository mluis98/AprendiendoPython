edades = [2, 4, 6, 8, 10, 12, 14, 16]
print "Hay " + str(len(edades)) + " edades."

numero = 4
if numero in edades:
	print "El valor " + str(numero) + " SI esta en el listado de edades."
else:
	print "El valor " + str(numero) + " NO esta en el listado de edades."


usuarios = ["Carlos", "Mishel", "Juan", "Cristina"]
print "Hay " + str(len(usuarios)) + " usuarios."

buscado = "Cristina"
if buscado in usuarios:
	print "La persona " + buscado + " SI esta en el listado de usuarios."
else:
	print "La persona " + buscado + " NO esta en el listado de usuarios."
