# El numero 0 se evalua como False
variable = 0
if variable:
    print "La condicion 1 es verdadera"
else:
    print "La condicion 1 es falsa"


# Cualquier numero que no sea cero se evalua como True
variable = -10
if variable:
    print "La condicion 2 es verdadera"
else:
    print "La condicion 2 es falsa"


# Un string vacio se evalua como False
variable = ""
if variable:
    print "La condicion 3 es verdadera"
else:
    print "La condicion 3 es falsa"


# Un string no vacio se evalua como Verdadero
variable = " "
if variable:
    print "La condicion 4 es verdadera"
else:
    print "La condicion 4 es falsa"


# Un string no vacio se evalua como Verdadero
variable = "Melvin"
if variable:
    print "La condicion 5 es verdadera"
else:
    print "La condicion 5 es falsa"


# Un valor no definido se evalua como False
variable = None
if variable:
    print "La condicion 7 es verdadera"
else:
    print "La condicion 7 es falsa"
