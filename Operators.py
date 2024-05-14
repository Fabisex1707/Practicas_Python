###Operadores Aritmeticos ###

"""""

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)

6+10 #esta operacion baiscamente no hace nada 

print(10 % 2) # este simbolo % nos ayuda a ver el residuo que deja una division # residuo=0
print(10 % 3) # residuo=1
print(12 % 7) # residuo=5
print(10 // 3) #floor division, pues lo que hace es darnos como resultado de una divison el numero entero mas cercano, en este caso 3 que anteriormente era 3.333333...
print(2 ** 3) #Elevar a un numero a x exponente #resultado = 8
print("Hola"+"Python") #aqui hemos hecho una Addition con la spabras como en en la union de conjuntos 
#print("Hola"-"Python") #Claro eso es una tonteria, con las cadenas de texto no tiene sentido, cosa diferente con las ecuaciones 

#print("Hola" + 5) aqui estamos cometiendo un error pues estamos mezclando diferentes tipos de datos, la manera correcta de hacer esto es por medio de la transformacion de datos 
print("Hola "+str(5)) #aqui estamo uniendo dos tipos de datos distintos, peroooo a uno lo estamos pasando de Int a Str por medio de una funcion...

print(10 + 3 -7 * 2 ** 3 //5) #aqui estamos combianando operaciones y al finalpara eso sirve python para hacer calculos más exactos... #Resultado= 2

print("Hola " * 5) #En este caso el hola se esta mosytrando 5 veces, pues le indicas a la maquina que lo multiplique
print("Hola " * (2**4)) #aqui de nuevo esta opracion hace que la palabra se replique varias veces, pero este no tiene mucho sentido  

#print("Hola" * 2.5) la replicacion no funciona con valores float
#print("Hola" *2.5*2) la replicacion no funciona con valores float, aqui sigue  siendo un valor float, pues 2.5 *2 = "5.0"
# print("Hola" *(2.5*2)) la replicacion no funciona con valores float, aqui sigue  siendo un valor float, pues 2.5 *2 = "5.0"
my_float = 2.5*2
#print("Hola" * my_int) la replicacion no funciona con valores float, aqui sigue  siendo un valor float, pues 2.5 *2 = "5.0"
print("Hola"* int(my_float)) #Ahora ya funciona pues el tipo de dato paso a ser de tipo Int de manera forzada 

###Operadores Comparativos###

print(3 > 4) #Mayor que
print(3 < 4) #Menor que
print(3 >= 4) #Menor o igaul que 
print(3 <= 4) #Mayor o igual que 
print(3 == 4) # iagual a 
print(3 != 4) # diferente que 
#print(3>4==2) esta comparacion nop tienen sentido pero podemos liogar varios signos de comparacion 
print("Hola" > "Python")
print("Hola" < "Python")
print("Hola" >= "Python")
print("Hola" <= "Python")
print("Hola" == "Hola")
print("Hola" != "Python")
#Todo el bloque pasado lo que esta comparando no es que la palabra es igaul que la otro o no o el numero de caracteres, sino que esta comparando el orden alfabetico de las palabras 
print("Hola">="Bola")
print("Hola" >="Zola") # Resultado= False, pq como dijimos Zola usa una letra que es mayor que una H de Hola 
print("aaab">="aaaa")
print("aaa" >= "AAA")
print(len("Hola") >= len("Python")) # aqui por la funcion len si que estamos comparando el tamaño de la cadena de texto

###Operadores Logicos###

print(3>4 and "Hola" > "Python") #False y False = Falsa hast que ambos sean True
print(3>4 or "Hola" > "Python") # False o False = False hast que ino sea True
#print(3>4 not "Hola" > "Python") aqui hay uin error pues nop se usa aqui

print(not(3>4))# este not nos ayuda a negar toda la comparacion (se muestra lo contrario)


print(3<4 and "Hola" < "Python") # True
print(3<4 or  "Hola" < "Python") #True


print(3>4 and "Hola" < "Python") #False
print(not(3>4 or "Hola" < "Python" and 4==3 or 45 != 45)) #True #Logica booleana 


"""

### Operators excersice-day 3###
"""""
#Excersice #1
base_tr=input("Please, give me a base for a triangle : ")
height_tr=input("Please, give me a height for a triangle : ")

resul= 0.5*(int(base_tr)*int(height_tr))

print(f"The area of the triangle  is: {resul}")
"""""
#excersice #2 
"""""
side_a=input("Please, give me a side for a triangle : ")
side_b=input("Please, give me another side for a triangle : ")
side_c=input("Please, give me another side for a triangle : ")

side = int(side_a)+int(side_b)+int(side_c)
print(f"the side of trangle is: {side}")
"""

#excersice #3

"""""

side_a=input("Please, give me a side for a  rectangle : ")
side_b=input("Please, give me another side for a  rectangle : ")
peremeter = 2*(int(side_a)+int(side_b))
area= int(side_a)*int(side_b)
print(f"the peremeter of rectangle is: {peremeter} and its area is: {area}")
"""

###excersice 4
"""""
print(1,    1,  1,  1*1,    1*1*1)
print(2,    1,  2,  2*2,    2*2*2)
print(3,    1,  3,  3*3,    3*3*3)
print(4,    1,  4,  4*4,    4*4*4)
print(5,    1,  5,  5*5,    5*5*5)

"""
a= 3
b=2
print(a + b) #addition 5
print(a-b) #subtraction 1
print(a/b)#division 1.5
print(a*b)# multiplication 6 
print(a**b)#exponentation 9
print(a//b)#floor divison 1


