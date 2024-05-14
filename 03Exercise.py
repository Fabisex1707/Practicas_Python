##Tuples### the tuples aren't moutables 
my_first_tuple=tuple()
my_first_tuple=("Fabisex","Eduardo","Olga","Alphonse","Negra","Violeta")
print(len(my_first_tuple))
family_members=my_first_tuple+("Pedro","Isabel")
print(family_members)
print(family_members[0:6])
print(family_members[6:])

fruits_tuple=("Mango","Banana","Melon","strawgberry","apple")
print(fruits_tuple)
vegetables_tuples=("mushroom","corn","radish","tomato","lettuce")
print(vegetables_tuples)
pet_food_tuple=("Pedigree","Freshpet","Fresh","Kibbles","Kibbles")
print(pet_food_tuple)
food_stuff_tp=fruits_tuple+vegetables_tuples+pet_food_tuple
print(food_stuff_tp)
print(len(food_stuff_tp))
print(food_stuff_tp[7])
print(food_stuff_tp[0:3])
print(food_stuff_tp[4:7])
del food_stuff_tp
#print(food_stuff_tp)

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
#print(nordic_countries.index("Estonia"))
#print(nordic_countries.index("Iceland"))
nordic_countries=list()#the tuple gets a list
print(type(nordic_countries))