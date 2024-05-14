###Tuples###
my_tuple = tuple()#esta es la amnera de definir una tuple
my_other_tuple=(30,60,40) #otra manera de definir una tuple, que es una tuple? es un cojunto de valores 

my_tuple=(35,1.50,"Fabi","Castro","Castro")
print(my_tuple)
print(type(my_tuple))
print(my_tuple[0])
print(my_tuple[-1])

#print(my_tuple[4]) #error
#print(my_tuple[-4]) #error
print(my_tuple.count("Castro"))#cuenta las veces que un valor se repite en la tuple #2
print(my_tuple.index("Castro"))# nos dice la posicion donde inica cierto valor 
print(my_tuple.index("Fabi")) #2

#my_tuple[1]= 1.80 #error
print(my_tuple)

####la gran diferencia enytre una lista y una tuple es que en la tuple no se pueden insertar nuevos valores, no se pude cambiar despues 

print(my_tuple+my_other_tuple) #aqui vemos que si vien no cambimaos la tuples si las unimos y podemos crea una nueva tuple con eso 
my_new_tuple = my_other_tuple + my_tuple
print(my_new_tuple) 
print(my_new_tuple[3:6])# aqui estamos partiendo en pedazos la tuple, la tuple crea constantes 

###tuple mutable? o lista? lo mejor es usar las co9sas para lo que fueron hechas, si quier4es que la tupla sea mutable conviertela a auna lista 

my_tuple=list(my_tuple) # si vas a definir un alista hazlo con la sentencia somethin=list(somethin) es mejor que solo somethin=[somethin]

print(type(my_tuple))
print(my_tuple)

my_tuple[4]=18 # esto no es para insertar un nuevo elemento esto es solo para cambiar el valor en una posicion que ya esta dada, cosa que no se pude hacer con las tuples
print(my_tuple)
my_tuple.insert(1,"Fabi's") # aqui SI esta mos insertando un NUEVO valor en la lista(antes tuple)
print(my_tuple)
### RECUERDA QUE ENTRE MAS INMUTABLE EL PROGRAMA MEJOR== MAS SEGURO ###
my_tuple=tuple(my_tuple) #convertimos de nuevo la list a una tuple con la sentencia tuple()
print(my_tuple) # <class 'tuple'>class: tuple

del my_tuple[4]
del my_tuple # esto es ilogico, pq una tuple no se modifica ni se borra, aqui borramos practicamnete la variable ya no existe
#print(my_tuple) # esto ahora es un error

