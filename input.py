"""
print("Dime lo que sea...")
anything = input()
print("Hmm...", anything, "... ¿en serio?")
"""

# el mensaje se mostrará en la consola antes de que el usuario tenga la oportunidad de ingresar algo
anything = input("Dime lo que sea...")
print("Hmm...", anything, "...¿en serio?")


# Probando un mensaje de error TypeError.
anything = input("Ingresa un número: ")
something = anything ** 2.0
print(anything, "al cuadrado es", something)

# Conversión de tipos 
anything = float(input("Ingresa un número: "))
something = anything ** 2.0
print(anything, "a la potencia de 2 es", something)

#calcula la longitud de la hipotenusa. Vamos a reescribirlo, para que pueda leer las longitudes de los catetos desde la consola.
leg_a = float(input("Ingresa la longitud del primer cateto: "))
leg_b = float(input("Ingresa la longitud del segundo cateto: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("La longitud de la hipotenusa es:", hypo)

# Operadores cadena
fnam = input("Me puedes dar tu nombre por favor? ")
lnam = input("Me puedes dar tu apellido por favor? ")
print("Gracias. ")
print("\nTu nombre es " + fnam + " " + lnam + ".")

# programa "dibuja" un rectángulo, haciendo uso del operador (+)
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n")*5, end="")
print("+" + 10 * "-" + "+")













