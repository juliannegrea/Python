# ######################## #
# TIPOS DE DATOS EN PYTHON #
############################

# PRIMITIVOS #

print("················································")
print("TIPOS DE DATOS PRIMITIVOS")
print("················································")

enter = 9
flotante = 7.4
cadena = "hola mundo"
boolean = True
print(type(enter))
print(type(flotante))
print(type(cadena))
print(type(boolean))


# OPERADORES ARITMÉTICOS #
print("················································")
print("OPERADORES ARITMÉTICOS (+),(-),(*),(/),(//),(**)")
print("················································")

suma = 2+5
resta = -66-55
mult = 8*9
div_coma = 3435/12
div_entera = 454//23
expon = 4**3

print("Suma + : " + str(suma))
print("Resta - : " + str(resta))
print("Multiplicacion * :"+str(mult))
print("Division Flotante / : "+str(div_coma))
print("Division Entera // : "+str(div_entera))
print("Elevacion: ** "+str(expon))

# OPERADORES COMPARACIÓN #
print("················································")
print("OPERADORES DE COMPARACION (==)(<)(>)(!=)(<=)(>=)")
print("················································")

x = 10
y = 88

print("== igual:" + str (x==y) )
print("<  menor:" + str (x<y) )
print(">  mayor:" + str (x>y) )
print("!= distinto:" + str (x!=y) )
print("<= menor_igual:" + str(x<=y) )
print(">= mayor_igual:" + str(x>=y) )

# OPERADORES LÓGICOS #
# estos operadores se usan para comparar valores TRUE y FALSE
# AND (and) devuelve True si ambas (ex1) y (ex2) son (True) después de comparar cada (ex1 = ex3) (ex2 = ex3)
# OR  (or)  devuelve True si al menos una de ex1 o ex2 sea True ((ex1=true) (ex2=false) ) = True
# NOT (not) devuelve lo contrario al resultado

print("················································")
print("OPERADORES LÓGICOS (AND) (NOT) (OR)")
print("················································")

var_1 = 56565
var_2 = 56565
var_3 = 56565

# compara var_1 == var_3 es true
# compara var_2 == var_3 es true
# resultado es True
resultado = var_1 and var_2 == var_3
print("NOT (ambos verdaderos) :" + str(resultado))

# OPERADORES TEXTOS #
# concatenacion +
# repeticion *



# OPERADORES IDENTIDAD #
# compara la posicion de memoria de dos objetos y no su contenido
print("················································")
print("OPERADORES IDENTIDAD (IS) (IS NOT)")
print("················································")

a = [1, 2, 3]
b = a
c = [1, 2, 3]
print("Resultado porque ocupan la misma posicion de memoria :")
print(a is b)
print("Resultado porque NO ocupan la misma posicion de memoria aunque tengan el mismo contenido:")
print(a is c)
print(type(a))







































# OPERADORES PERTENENCIA #
#print("················································")
#print("OPERADORES PERTENENCIA")
#print("················································")
