num1=input("ingrese el primer numero: ")
num2= input("ingrese el segundo numero: ")
num3= input("ingrese el tercer numero: ")
if int(num1) > int(num2) and int(num1)> int(num3):
  print("El numero mayor es: ", num1)
elif int(num2) > int(num1) and int(num2) > int(num3):
   print("El numero mayor es: ", num2)  
elif int(num3) > int(num1) and int(num3) > int(num2):
  print("El numero mayor es: ", num3)
else:
  print("ningun numero es mayor")