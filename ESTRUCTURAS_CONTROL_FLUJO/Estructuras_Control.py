import keyword

print(".............................................................")
print("ESTRUCTURAS CONTROL FLUJO")
print(".............................................................")
print(" IF 			 --> comprueba exp , si esta es True ejecuta algo ")
print(" IF-ELSE    --> comprueba exp si esta es True ejecuta algo si es False ejecuta otra cosa ")
print(" ELIF 		 --> se combina con el if para comprobaciones múltiples pasa a ejecutar siguente instruccion siempre que la expresion de antes es False ")
print(".....................")
print("EJERCICIOS")
print(".....................")


num_1 = 4
num_2 = 5555555

if num_1 == num_2 :
	print("son iguales")
elif  num_1 < num_2 :
	print("numero 1 es mayor que num 2")
elif num_2 > num_1:
	print("numero 2 es mayor que num 1")

# Ejercicio 1
# Realiza un programa que lea dos números por teclado y permita elegir entre 3 opciones en un menú:
# Mostrar una suma de los dos números
# Mostrar una resta de los dos números (el primero menos el segundo)
# Mostrar una multiplicación de los dos números
# En caso de introducir una opción inválida, el programa informará de que no es correcta.


eleccion = {
    1: "suma",
    2: "resta",
    3: "mult"
}

print (type(eleccion))

sumar = 1
restar = 2
mult = 3

n1 = input("n1:")
n2 = input("n2:")
n4 = input("Elige:")

if	(eleccion == 1) :
	print(n1+n2)
elif (eleccion == 2):
	print(n1 - n2)
elif (eleccion == 3):
	print(int (n1) *int (n2))
