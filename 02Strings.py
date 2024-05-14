print("Thirty", "Days", "Of", "Python")
print("Coding","For","All")
company="   Coding for all   "
"""""
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())# vuelva la primera letra de cada palabra en maytucula 
print(company.swapcase())
company_slice=company[1:14]
print(company_slice)
print(company.startswith("Coding"))
print(company.find("Coding"))
print(company.index("Coding"))

company_slice_two=company[7:14]
company_two=(f"Python {company_slice_two}")
print(company_two.replace("Python","Everyone"))#replace nos ayuda a remplasar una naterior palabara por una nueva

print(company_two.split())
print(type(company_two.split()))# con el.split podemos crea una lista de una cadena de texto number 13
more_company="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(more_company.split())
print(company[0])

print(company[10])

pfe="Python For Everyone"

print(pfe[0],pfe[7],pfe[11:18])# aqui estamos haciendo abreviaturas para nuestras frases con ayuda de las posiciones 

print(company[0],company[7],company[11:])# aqui estamos haciendo abreviaturas para nuestras frases con ayuda de las posiciones 

print(company.index("C"))
print(company.index("f"))

search="You cannot end a sentence with because because because is a conjunction"
print(search.index("because"))#estas funciones nos ayudan a encontrar la posicion de cierta letra como tal, pq la palanbara entera no la puede determiunar del todo sola #index:31
print(search.find("is"))#estas funciones nos ayudan a encontrar la posicion de cierta letra como tal, pq la palanbara entera no la puede determiunar del todo sola  #index:31
slice_conjuntion=search[31:54] #AQUi lo que estamos haciendo es guarade el rago de carateres del [31 al 54] en un avarables para poder convertirala en una lista
print(slice_conjuntion.split())
print(search.rindex("because"))#aqui usamos reindex para saber en que posicion se encuentra la ultima aparicion de "Because"

print([search[0:30]+search[54:]])

print(search.index("because"))
print(company.startswith("Coding"))
print(company.endswith("Coding"))

"""
""""
print(company[3:17])

val_one="30DaysOfPython" #indetifier este consiste en una variable que cumple con la escritura (letras (a-z(mayus or mini))"_"(0-9)) debe de cumplir si o si con el roden pero las "_" es opcional
val_two="thirty_days_of_python"

print(val_one.isidentifier())
print(val_two.isidentifier()) #32
"""

python_libreris=["Django", "Flask", "Bottle", "Pyramid", "Falcon"]
print(python_libreris)
print("I\nam\nenjoying\nthis\nchallenge")
print("I\njust\nwonder\nwhat\nis\nnext.")


print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")


radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square.")
print("The area of a circle with radius {} is {} meters square.".format(radius,area))

number_one=8
number_two=6
resul_one= 8+6
print("{}+{} = {}".format(number_one,number_two,resul_one))
resul_one= 8-6
print("{}-{} = {}".format(number_one,number_two,resul_one))
resul_one= 8*6
print("{}*{} = {}".format(number_one,number_two,resul_one))
resul_one= 8/6
print("{}/{} = {}".format(number_one,number_two,resul_one))
resul_one= 8%6
print("{}%{} = {}".format(number_one,number_two,resul_one))
resul_one= 8//6
print("{}//{} = {}".format(number_one,number_two,resul_one))
resul_one= 8**6
print("{}**{} = {}".format(number_one,number_two,resul_one))

