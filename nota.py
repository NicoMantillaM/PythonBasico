# Entrada de notas
notac1 = int(input("Ingrese su nota del certamen 1: "))
notac2 = int(input("Ingrese su nota del certamen 2: "))
notalab = float(input("Ingrese su nota de laboratorio: "))
 
nc= (60 - (notalab* 0.3))/ (0.7)
n3= (nc*3) - (notac1 + notac2)

print(f"La nota que necesita en el tercer certamen es igual a:{n3}")