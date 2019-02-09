# Primer programa con Python
import pyperclip

CLARO = 'abcdefghijklmnopqrstuvwxyz'
CIFRADO = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'

salida = ''

texto = input('Introduce un texto \n')
for simbolo in texto.lower():
	if simbolo in CLARO:
		indice = CLARO.index(simbolo)

		salida += CIFRADO[indice]

print(salida)
pyperclip.copy(salida)
#Esto es una prueba de la vendimia joder
##Vuelve a leer dafnis y cloe
#Plox