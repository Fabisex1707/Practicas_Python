###Strings###
my_string = "Mi string"
my_other_string = "Mi string"

print(len(my_string))
print(len(my_other_string))

print(my_string + " "+ my_other_string)

my_new_line_string="este es un string \n con salto de linea" #el \n sirve para dar un salto de linea
print(my_new_line_string)

my_tap_string="\t este es un string con salto de linea" #el \t sirve para dar un marguen  
print(my_tap_string)

my_scape_string="\t este es un string \n escapado" #el \n sirve para dar un salto
print(my_scape_string)

my_scape_string="\\t este es un string \\n escapado" #si ponemos dos \\ a la n y t todo se cancela y no sirve el salto ni la tabulacion...
print(my_scape_string)

###Formateo###
#Estos formateos nos ayudan a escribir cadenas de texto mucho mas limpias

"""""
igual que aqui, es mas feo usar todas esa comillas que solo usar el format o la %s y %d
elif int(my_may_1)<=10 or int(my_may_2) > int(my_may_1) or int(my_may_3)!=100:
    print("your number1. "+my_may_1+" is menor or igual than 10, or your number2: "+my_may_2+" is mayor than your number1, or your number3: "+my_may_3+" is different to 100")
"""

name,surname,age ="Fabi", "Dolores", 19
print("Mi nimbre es {} {} y mi edad {}".format(name,surname,age))#no olvides que con el punto format no hay necesida de usar %s o %d solo {}

print("Mi nimbre es %s %s y mi edad %s"%(name,surname,age)) #la mejor forma de hacer cadenas de texto usando variables, pues de esta manera se contrla el tipo de datos que resivas 
#print("Mi nimbre es %s %s y mi edad %d"%(name,surname,"Hola")) # aqui nos marca un error, pues el dato que le estamos pasando es str y no int como se esperaba, este formna de encadenas palabras y variables nos ayuda a mantener coherencia con los tipos...
 ### %s== String, %d==Int, %f==Float
 #Otra manera de pasar datos SIN formatear (psar datos tal cual)
print(f"Mi nimbre es {name} {surname} y mi edad {age}")
print(type(f"Mi nimbre es {name} {surname} y mi edad {age}")) #Type str, pues literalmente imprime una cadena de string

### Desempaquetado de caracteres###
#lo que intentamos hacer es descomponer la palbar en letras de una en una 
langauge ="python" 
a,b,c,d,e,f = langauge
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

print(a)
print(e)

##division

langauge_slice=langauge[1:3]
print(langauge_slice) # de las leytras que tenemos de la palbra Python nos da solo el de la posicion 1 y 2, pues no contamos al 3

langauge_slice=langauge[1:] # si nostros ponemos solo desde donde comienza a agarrar numeros sin ponerle el limite la maquina agarrara todas las demas #ython
print(langauge_slice)

langauge_slice=langauge[-2]# aqui estamos haciendo una regresion de la ultima letras a la priemra la que esta en la posicion -2 es o
print(langauge_slice)

langauge_slice=langauge[0:6:2]# aqui estamos haciendo un salto de ciertos caracteres, pues agarramos el  0=p y el 2=t
print(langauge_slice)


###Reverse

reversed_language= langauge[::-1] # lo estamos haciendo es poner la palabra al reves 
print(reversed_language)

###funciones 

print(langauge.capitalize())#esta funcion nos poen en mayuscula el primer caracter
print(langauge.upper())#esta funcion nos ayuda a que todos los caracteres sean mayusculas
print(langauge.count("t")) # nos aqyuda a contar cuantos caracteres tenemos peor le teines que especificar que caracter quieres que cuente
print(langauge.isnumeric()) # nos ayuda a determinar si un valor es un numero o no 
print("1".isnumeric())# nos ayuda a determinar si un valor es un numero o no 
print(langauge.lower())
print(langauge.upper().isupper()) # aqui lo que estamos haciendo es convertir en mayuscula la palabra"python" y luego revisar si la cadena de texto esta tdo el mayusculas
print(langauge.lower().isupper()) #False
print(langauge.startswith("py")) # esta fucion nos ayuda a verificar que una cadena de texto empiece con ciertos caracteres #util en contraseñas jkfhskdjh
print(langauge.startswith("PY")) # aqui nos indica que la palbra python empieza con PY y no es cierto, pues no es lo mismo py==PY

print("py"=="PY") #NO es lo mismo minusculas que mayusculas

