# Entrada de notas
notac1 = int(input("Ingrese su nota del certamen 1: "))
notac2 = int(input("Ingrese su nota del certamen 2: "))
notalab = int(input("Ingrese su nota de laboratorio: "))
 
notalab2= int(notalab)*0.3
notamin= 60
notac= notamin-notalab2
notaca= notac/0.7

#hallar nota certamen3
suman1n2= int(notac1)+ int(notac2)/3
notan3= int(notaca)*3
notan3cal= int(notan3)- int(suman1n2)
n3aprox= round(notan3cal)

#calcular promedio certamen
notacertamen= int(notac1)+int(notac2)+int(n3aprox)/3

#calcular nota ramo
notaramo= int(notacertamen)*0.7 + int(notalab2)
notac3=notaramo

#mostrar nota min
if notaramo>=60:
    print(f"Ya pasaste el ramo con: {notaramo}")
else:
    if n3aprox<=100:
        print(f"Debes sacar minimo:", int(n3aprox), f"en el certamen 3 para aprobar el ramo con:{notac3}")
    else:
        print(f"No tienes posibilidad de pasar el ramo")