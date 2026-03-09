# Ejercicio 1

var_texto = 'Esto es un texto'
var_numero = 17
var_lista = ['Luis', 35, False]
var_boolean = True


#Ejercicio 2

var_texto = 'Esto es un texto'
var_substring=var_texto[:3]

print(var_substring)

# Ejercicio 3

var_lista = ['Luis', 35, False]
var_elemento = var_lista[0]

print(var_elemento)

# Ejercicio 4

var_numero = 17
var_total = var_numero + 10

print(var_total)

# Ejercicio 5

var_lista = ['Luis', 35, False]
var_elemento = var_lista[-1]

print(var_elemento)

# Ejercicio 6

names = 'harry,alex,susie,jared,gail,conner'
names_split = names.split(',')

print(names_split)



# Ejercicio 7

var_texto = 'Esto es un texto'
var_substring = var_texto[:4]
var_substring = var_substring.upper()
var_texto_final = f'{var_substring}{var_texto[4:]}'

print(var_texto_final)


# Ejercicio 8

var_numero = 17
var_posicion = f'Tu posición es la número {var_numero}'

print(var_posicion)


# Ejercicio 9

print('hello world')


# Ejercicio extra

var_saludo = 'y entonces dijo: Hola compañeros'
query = var_saludo.find('Hola')
Var_saludo2 = var_saludo[17:21]
var_saludo = var_saludo.replace('Hola', 'adiós')

print(var_saludo)
