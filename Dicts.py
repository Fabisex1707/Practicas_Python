###Dictionaries###

my_dict = dict() #creation of dictionary
print(type(my_dict))

my_other_dict ={} #remeber when you use the {} the data type is Dict==dictionary 
print(type(my_other_dict))

my_other_dict={"Nombre":"Fabi", "Apellido":"Castro", "Edad":"18", 1:"python"} #this estructre is the difference between a set and dictionary :D
###how you can see every type has a ID type String but the last in line is a Int, but it's okay Python is so cool

my_dict={
    "Nombre":"Fabi", 
    "Apellido":"Castro", 
    "Edad":"18", 
    "languages":{"python","Siwft","Kotlin"}, # <--- This is a set wow :o
    1:1.50
}

print(my_other_dict)
print(my_dict)
print(len(my_other_dict))
print(len(my_dict)) # len == 5 because every ID is counted

print(my_dict["Nombre"]) #here´s find a specific data in my_dict

my_dict["Nombre"] = "Pedro"#here's changues the value of a piece of date  
print(my_dict["Nombre"])

#print(my_dic["1"]) #remeber if you want find a index you most write well

print(my_dict[1])

my_dict["Calle"]="Pino de Arizona" #here´s adds a new date in the dictionary 

print(my_dict) #{'Nombre': 'Pedro', 'Apellido': 'Castro', 'Edad': '18', 'languages': {'python', 'Siwft', 'Kotlin'}, 1: 1.5, 'Calle': 'Pino de Arizona'}

del my_dict["Calle"] #this is the way to delete a date in the dictionaries :D
print(my_dict) #{'Nombre': 'Pedro', 'Apellido': 'Castro', 'Edad': '18', 'languages': {'python', 'Kotlin', 'Siwft'}, 1: 1.5}

#print("Pedro" in my_dict) #this way you must find for a Index not for a character 
#print("Fabi" in my_dict)

print("Apellido" in my_dict) #becuase the index Apellido is there 
print(my_dict["Apellido"]) #this way yuou can see the value of the index Apellido

print(my_dict.items())#The funtion give us a set with  the dates and indexes of my_dict 
print(my_dict.keys())#The funtion give us a set with  the indexes of my_dict 
print(my_dict.values())#The funtion give us a list with  the dates of my_dict 
print(my_dict.fromkeys(("Nombre", 1)))

my_new_dict =my_dict.fromkeys(("Nombre",1,"Piso")) # this funtion let us a new dictionary with last keys wow :v // You don't need to create a dictionary based on another
print(my_new_dict) 

my_list=["Nombre",1,"Piso"]  # you can create a dictionary based on a list 

my_new_dict =dict.fromkeys((my_list)) # you can create a dictionary based on a list 
print(my_new_dict)
my_new_dict=dict.fromkeys(("Nombre",1,"Piso")) # you can create a dictionary based on a list or NO jkfhsdkjh
print(my_new_dict)

#my_new_dict= dict.fromkeys(my_dict,("Fabi","Castro")) #this is way you can create a dict very fast, because all of the  indexes are copied in a my_new_dict
my_new_dict= dict.fromkeys(my_dict) #you can't add to the new dict eny value, bacuse the dict doesn't know what's the order 
print(my_new_dict)

my_new_dict["Nombre"] = "Violeta"
print(my_new_dict)