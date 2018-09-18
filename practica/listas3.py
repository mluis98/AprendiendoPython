chapines = ["Juan", "Mateo", "Rosa", "Rafael", "Celia"]
mexicanos = ["Cristian", "Rolando", "Roselia", "Mary"]
gringos = ["Timothy", "Paul", "Christopher", "July", "Karly"]

persona = raw_input("Ingrese un nombe: ");
if persona in chapines:
	print "es Guatemalteco"
elif persona in mexicanos:
 	print "es mexicano"
elif persona in gringos:
	print "es estadounidense"
else:
	print "desconocido"			