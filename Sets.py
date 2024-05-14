### Sets ####

my_set= set() #here's create the set
my_other_set= {}
print(my_set)
print(type(my_set))#class 'set'
print(type(my_other_set)) #class 'dict' or class 'set'?

my_other_set= {"Fabi","Castro",18} # when we start de funtion this starting as a Dictionary, but when you fil it with this way, the type of the data gets a set :v
print(my_other_set)
print(type(my_other_set)) # now it's a set WTF kjfdhwsjk

print(len(my_other_set)) #3 items
#print(my_other_set[0]) #error this way we can´t to access to the items to the set because there's not a order in the sets 
my_other_set.add("Fabi's") 
print(my_other_set) #here we can watch in the set the things order is different {'Fabi', 18, 'Castro', "Fabi's"} when most be {'Fabi', 'Castro',18, "Fabi's"} ???. Set isn't a order estructure
my_other_set.add("Fabi's") #A set doesn't want repeated things
print(my_other_set) #a set is moutable 

print("Fabi" in my_other_set) #true because Fabi exist in the set 
print("Fabe" in my_other_set)#False becuase Fabe doesn't exist in the set 
my_other_set.remove("Fabi") #here we can delete a item, you have to remember in a set, we dont acces to their items and a set there's not  an order.
print(my_other_set)
my_other_set.clear()
print(my_other_set) #set is empty ;'v
print(len(my_other_set)) # items = 0

del my_other_set # here we deleted to the set OMG!
#print(my_other_set)# and here there's a error, because we deleted to the set 

my_set ={"Fabi","Castro",18} #here we're getting a set to a list 
my_list =list(my_set)
print(my_list)
print(my_list[0])# this is not well, because if we know what's the possition of the tings with a set the possition is always going to change! 

my_other_set={"Python","Kotlin","c++"}

my_new_set=my_set.union(my_other_set) #Here we're tying one set together with another
print(my_new_set.union(my_new_set)) #remeber a set doesn't want repeated things
print(my_new_set.union(my_new_set).union(my_new_set.union({"Java","C#"})))#here the set accepts Java and c# because they are different from the others
print(my_new_set.difference(my_set)) #aqui podemos ver las diferencias que hay entre my_new y my_set en la consola arroga solo los que son diferentes! 
print(my_new_set.issuperset(my_other_set)) #esta funcion nos dice si un set es "superior" que otro true or false #True
print(my_other_set.issubset(my_new_set)) #esta funcion nos dice si un set es "inferior" que otro true or false #True
print(my_new_set.issubset(my_other_set)) #false 
print(my_other_set.isdisjoint(my_new_set)) #False because Both sets have things in common
print(my_set.isdisjoint(my_other_set))
