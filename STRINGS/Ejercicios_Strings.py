# 1 Escribir un programa que pregunte el nombre del usuario en la consola y un número
# entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces
# como el número introducido.
from datetime import datetime
from itertools import product
from sys import prefix

#name_user = (input("Introduce tu nombre de usuario: "))
#aux = (input("Introduce las veces que quieres mostrar tu nombre de usuario:"))

#for i in range(int(aux)):
   # print(name_user)

# Escribir un programa que pregunte el nombre completo del usuario en la consola y
# después muestre por pantalla el nombre completo del usuario tres veces, una con to
# das las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la pri
# mera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir su
# nombre combinando mayúsculas y minúsculas como quiera.

#nom = (input("Introduce tu nombre completo: "))
#print("Mayusculas: " + nom.upper() )
#print("Minusculas: " + nom.lower() )
#print("Primera letra mayus: " +nom.title())

# Escribir un programa que pregunte el nombre del usuario en la consola y después de
# que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras,
# donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras
# que tienen el nombre.

#nom = (input("Introduce tu nombre: ").upper())
#print (nom +" tiene una longitud de " +  str (len(nom)))

# Los teléfonos de una empresa tienen el siguiente formato prefijo-número-exten
# sion donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por
# ejemplo +34-913724710-56). Escribir un programa que pregunte por un número de
# teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.

#nr = input("intro numero con este formato yyxxxxxxzz: ")
#print(nr[2:])

# Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.
#frase = input("intro una frase: ")
#print(frase[::-1])

# Escribir un programa que pida al usuario que introduzca una frase en la consola y una
# vocal, y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.

#frase = input("intro una frase y una vocal: ")
#vocal = input("intro vocal:")
#print("La frase es: " + frase + "y la vocal mayus es: " + vocal.upper())

# Escribir un programa que pregunte el correo electrónico del usuario en la consola y
# muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante d
# la arroba @) pero con dominio ceu.es.

#email = input("email: ")
#email_dom = email + "@ceu.es"
#print(email_dom)

# Escribir un programa que pregunte por consola el precio de un producto en euros con
# dos decimales y muestre por pantalla el número de euros y el número de céntimos del
# precio introducido.

#precio = input("precio: ")
#euros = precio [0 : precio.find(".")]
#centimos = precio [3::]
#print("Son {} euros y {} centimos " .format(euros, centimos))

# Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato
# dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa ante
# rior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.


#fecha = input("Introduce la fecha de su nacimiento formato dd/mm/yy : ")
#dia = fecha[:fecha.find("/")]
#mes = fecha[3:5]
#ano= fecha[6::]
#print(dia, mes, ano)

# Escribir un programa que pregunte por consola por los productos de una cesta de la
# compra, separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.

#lista_compra = input("Lista productos: ")
#print(lista_compra.replace(" ", "; \n"))

# Escribir un programa que pregunte el nombre el un producto, su precio y un número
# de unidades y muestre por pantalla una cadena con el nombre del producto seguido
# de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con
# de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con

nombre_producto = input("Nombre producto: ")
precio_producto = input("Precio producto: ")
unidades_producto = input("Unidades producto: ")

print("El producto " + nombre_producto + " con precio " + precio_producto [1:9] + " euros y unidades " + unidades_producto [1:9] + " esta agotado")
