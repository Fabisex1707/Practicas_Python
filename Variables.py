#variables 

#Myvariable ="my string variable" ESTA FORMA DE ESCRIBIR LAS VARIABLES ES INCORRECTA, SIEMPRE SE ESCRIBE CON MINUSCULAS Y CON "_"
my_string_variable ="Hello"
print(my_string_variable)

my_int_variable = 4 #para definir el tipo de dato de la variable solo basta con poner el valor, ya sea numerico,string, bool...
print(my_int_variable)

#ENCADDENAMIENTO DE VARIABLES EN PRINT

print(my_int_variable,my_string_variable) #aqui encademanos las variables en un solo print

#CONVERSION DE UN TIPO DE DATO A OTRO 
my_int_str_variable= str(my_int_variable) #aqui estamos creando una nueva variable y el valor que le asignamos es un INT pero con "str" lo vamos a pasar a string
print(my_int_str_variable) #aqui se inprime el valor de la variable que creamos arriba, ahora es un string = "5"
print(type(my_int_str_variable)) #aqui estamos pidiendo con type el tipo de dtao que tiene como valor "my_int_str_variable"
print(type(print(type(my_int_str_variable)))) # TIPO 'NoneType' esto es muy muy redundante asi que Python se muere del asco 

#Funciones del sistema 
print(len(my_string_variable)) #len nos ayuda a contar los caracteres que contiene cada variable 

print("Este es el valor de :",my_string_variable)

#VARIABLES EN UNA SOLA LINEA

name, surname, alias, age ="Fabian", "Castro", "Fabisex",18
print("Mi edad es:",age,"Mi alais es:",alias,"Mi nimbre es:",name,"Mi apellido es:",surname) #aqui nostros estamos deifiniendo variables en una sola linea, aunque sea cool no es lo mejor


#Imputs //Lo mejor del mundo kjhdskjafhk

#first_name= input("What's your name? ") # definimos una varbles a la cual se le pide que le ingreses datos 
#ge = input("How old are you? ") # definimos una varbles a la cual se le pide que le ingreses datos 


#print(first_name) #se inprime el valor que se le colocó a la varable en el input
#print(age) #se inprime el valor que se le colocó a la varable en el input

# aqui vamos a hacer un Input con las varables anteriores 
#name=input("What's your name? ")
#alias=input("What's your alias? ")

#print(name)
#print(alias)

# como ya sabemos las variables pueden ir cambiando de valor conforme avance la ejecucion 

name = 36
age= "FABI"
print(name)
print(age)

#Python no es de tipado fuerte puese le pueden meter cualquier tipo de dato en ejecucion 

address:str="Mi direccion" #No importa si aclaras que es de un cierto tipo de dato, a python le pudes modificar el valor en ejecucion 
address = 32
print(address)

#Este tipo de probelmas solo ocurren cuando no se estan usando de manra mas especifa las variables como en un input, pues aqui si que debes de poner un tipo especifico de dato...