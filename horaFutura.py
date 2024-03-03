horac=int(input("Ingrese la hora actual, segun la hora militar y sin ingresar los minutos: "))
horas= int(input("Ingrese la cantidad de horas que desea avanzar"))
horava= int(horac) + int(horas) % 24
print (f"Las horas transcurridas despues de la hora: {horac}, segun la cantidad de horas: {horas}, es igual a: {horava}")


