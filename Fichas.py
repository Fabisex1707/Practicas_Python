### Lists ###

my_list = list () #una lista nos ayuda a crear una estructura == array, en las list se hacen operaciones mucho mas complejos###Forma 1 de definir una lista
my_other_list= [] #forma 2 de definir una lista

print(len(my_list)) #aqui estamos imprimiendo nuestra lista para ver los elementos que tenemos y con el len vemos cuantas operaciones o datos ya tenemos

my_list= [35, 45, 64, 54, 54, 32, 90]
print(len(my_list))

my_other_list = [35, 1.77,"fabi","sex"] #aqui podemos ver que en python se pueden agregrar distintos tipos de datos en una sola lista
print(type(my_other_list)) # aqui ya vemos que al momento de ver el tipo de dato en una lista es Type# list

print(type(my_list))
print(type(my_other_list)) # debes de recordar que un array no es igual que una lista, pues la lista es mucho mas completa que un array


print(my_other_list[0])
print(my_other_list[-1]) # en eta linea lo que estamos haciendo es sacar datos por separado de las listas 
print(my_other_list[-3])
print(my_other_list[-4])
print(my_list.count(54)) #el count en primera nos retorna la frecuencia en la que se repite un valor  #2
print(my_other_list.count("fabi")) # aqui count me dice que 1 vez se repite la cadena "fabi"
#print(my_other_list[-5]) # aqui estamos viendo que para las listas solo podemos sacar los datos con posiciones validas, si solo tines 0,1,2,3, no pudes bucar el 4 o el -4

#age , height, name, surname = my_other_list #los nosmbres de las varaibles no toene ese nombre pq el programa sepa que datos corresponde, tambien para poder asignarles variables a un alista debes de asignarselas a todas, si son 3 entonces 3 variables, de lo ocntrario el programa is dead
height, name, age ,  surname = my_other_list[1],my_other_list[2],my_other_list[0],my_other_list[3] # esto de difinar a cada varable cual sera su valor dentro de la lista es muy rebuscado, pues es posible foco de errores
print(surname)

print(my_list + my_other_list) # aqui lo que hemos hecho es sumar los valores que tienen dos listas :o
#print(my_list - my_other_list) # error
#print(my_list * my_other_list) # error


my_other_list.append("Favidev") # aqui con el .append agregamos, pero el dato se va al final 
print(my_other_list)

my_other_list.insert(1,"azul")# con .insert lo que podemos hacer es garegar cosas a ala lista peor tambien darlke la posicion que queremos
print(my_other_list)

my_other_list.remove("azul") #.remove nso ayuda a eliminar datos de la lista 
print(my_other_list)

my_list.remove(54) #aqui con ayuda de .remove estamos eliminando uno de los numeros que estaban repetidos 
print(my_list)

#my_list.pop() # el pop lo que hace es eliminar de la lista el ultimo numero que tengamos
print(my_list.pop())# aqui lo que estamos haciendo es imprimer el pop y por secuente nos dará el numero que quito, pero que al final siempre devuelve 

#print(my_list.pop(2))# aqui lo que hacemos con el pop es indicrale la posicion que queremos que elimine 

my_pop_elemnt = print(my_list.pop(2))
print(my_pop_elemnt) #al final podemos guarda en una varable el numero que borró

## muy importante, el remove , el pop y el del == delete no es lo mismo, son cosas diferentes y claro puede parecer que pop por decirle cual puedes eleminar crees que funciona igual que el del pero no, recuerda que pop retorna el valor para que lo uses de alguna manera y el otro solo lo elimina
del my_list[0]##elimina por indice==numero de posicion
print(my_list)

my_new_list=my_list.copy()#aqui con copy estamos haciando un arespaldo de los valores de my_list en una nueva lista my_new_list, hay que tomar en cuenta que esta lista sera igual que la anterior solo en es epunro del codigo, si agragamos un nuevo elemento o eliminamos la lsita no importa

my_list.insert(2,"verde") # aqui con insert lo que hacemos es insertar un nuevo valor en la lista, esto especificando el indice en el que queremos quee este y el dato (Index,Int,Str...)
print(my_list)
print(my_list.index("verde"))

my_list.clear() #utilizamos la funcion .clear para limpiar todos los datos de la lista, ojo la lista aun existe solo que ahora esta vacia
print(my_list)
print(my_new_list)


my_new_list.reverse()# aqui lo que estamos haciendo es invertir el roden de los valores en la lista
print(my_new_list)



my_new_list.sort() # aqui tenemos la fun sort a la cual le podemos dar criterios de ordenacion pues si lo usamos solo este orde de menor a mayor o en orden alfabetico
print(my_new_list)

print(my_new_list[0:3])# de esta manera lo que hacemops es cortar una lista en pedazos 

print(my_new_list)
my_new_list[1]=78
print(my_new_list)



my_list ="Hi Python" # nostros al hacer esto hemos cambiando el tipo de dato que era la lista, debes de poner [] para que enmtienda que es una lista 
print(my_list) 
print(type(my_list)) #Type: str
