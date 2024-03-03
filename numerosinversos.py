numero= input("ingrese un numero entero de tres digitos: " )
if len(numero) != 3:
   print("el numero ingresado no es valido, intentelo denuevo")
else:
   digitos= list(numero)
   digitosinver= digitos[::-1]
#convertir la lista de numeros inversos en un numero denuevo
   numerosinver= int("".join(digitosinver))
print ("El digito con los numeros inversos es: ", numerosinver)

