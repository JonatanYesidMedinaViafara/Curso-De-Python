#Curso de la variables
"""
Recuerda que existen diferentes variables
"""
#manera de escribir con una variables
#tener en cuenta no se debe nombra de manera diferente
#a esto, es decir con mayuscula y minusculas
my_string_variable="my string variable"
print (my_string_variable)

my_int_variable=2
print(my_int_variable)

my_boot_variable=False
print(my_boot_variable)

#se esta haciendp un preinterprete

#nueva manera de imprimir en print

#concatenacion
print(my_boot_variable, my_int_variable,my_string_variable)

#se puede cambiar el tipo de una varible si se antepone una tipo en parentesis
#ejemplo
my_int_to_str_variable=str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

#funciones del sistema
#uso del len
print(len(my_int_to_str_variable))

print("vamos concatenar un print ",my_boot_variable  )

#variables en una sola linea
name, surame, alias ="jonatan ", "Yesid ", "Medina"
print("me llamo: ", name , surame, "y mi alias es ", alias)
"""
name2=(input("what your name: "))
lastname=(input("what your last name: "))

print("your name complete is ", name2 , lastname )
"""
#cambiando datos de las variables
#es facil cambiar los datos a las variables de python
"""
name2=(input("what your name: "))
lastname=(input("what your last name: "))

print("your name complete is ", name2 , lastname )
"""
#forzamos el tipo
address: str="Yolo"
address=5
print(address)

#coomo consultat el tipo de dato
print(type("soy un dato str"))
print(type(5)) #tipo int
print(type(1.5)) #tipo float
print(type(3+2)) #tipo complex
print(type(True)) #tipo "boot"
print(type(print("mi cadena de texto"))) #tipo NoneType