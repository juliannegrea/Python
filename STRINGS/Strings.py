# STRINGS #

my_string = "hola que tal estas , aprendemos los strings"


#ATRIBUTOS#

#capitalize(): devuelve una copia de la cadena con la primera letra en mayúscula y el resto en minúscula.")
print(my_string.capitalize())
#lower(): devuelve una copia de la cadena con todas las letras en minúscula
print(my_string.lower())
#upper(): devuelve una copia de la cadena con todas las letras en mayúscula.
print(my_string.upper())
#title(): devuelve una copia de la cadena con todas las letras en mayúscula.
print(my_string.title())
#strip(): devuelve una copia de la cadena con los espacios en blanco eliminados al principio y al final.
print(my_string.strip())
#split(): devuelve una lista de las palabras de la cadena separadas por espacios en blanco.
print(my_string.split())
#join(iterable): devuelve una cadena que es la concatenación de los elementos de un iterable (por ejemplo, una lista o una tupla), separados por la cadena original.
#al final de cada strings pone lo el primero caracter que le hayas puesto , y luego el segundo y asi succesivamente
print(my_string.join(" ABC"))
#replace(old, new): devuelve una copia de la cadena con todas las apariciones de la subcadena "old" reemplazadas por la subcadena "new".
print(my_string.replace("o", "A"))
#count(substring): devuelve el número de veces que la subcadena "substring" aparece en la cadena.
print(my_string.count("a"))
#startswith(prefix): devuelve True si la cadena comienza con el prefijo especificado, de lo contrario, devuelve False.
print(my_string.startswith("hola"))
#endswith(suffix): devuelve True si la cadena termina con el prefijo especificado, de lo contrario, devuelve False.
print(my_string.endswith("strings"))
#index(substring): devuelve el índice de la primera aparición de la subcadena "substring" en la cadena. Si no se encuentra, se genera una excepción ValueError.
print(my_string.index("strings"))
#find(substring): devuelve el índice de la primera aparición de la subcadena "substring" en la cadena. Si no se encuentra, devuelve -1.
print(my_string.find("strings"))



#METODOS#



#FORMATEO#
#name, surname, age = "Iulian", "Negrea", 27
#print("Mi nombre es {} mi apellido es {}  y mi edad es {}".format(name,surname,age))
#print("Mi nombre es %s mi apellido es  %s  y mi edad es  %s" % (name,surname,age))
#print("Mi nombre es " + name + surname + "y mi edad es" + " " + str(age) )
#print("Me cago en tu puta madre \n \t\thijo de la gran puta" )

