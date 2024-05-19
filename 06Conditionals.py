###Conditionals Exercise###
"""""
age = input("Enter your age: ")


if int(age) >= 18:
    print("Yo're old enough to learn to drive")
else:
    difference_age = 18 - int(age)
    print(f"You need {difference_age} more year(s) to learn to drive")
    """""

"""""
input("who is older?")
age_one =input("How old are you?")

if int(age_one) > 30:
    difference = int(age_one) - 30
    print(f"You  are {difference}  year(s) older than me")

elif int(age_one) == 30:
    print("we're the same age")

else:
    difference = 30 - int(age_one)
    print(f"i'm {difference}  year(s) older than you")
"""""
"""""
number_a =input("Give me a number")

number_b =input("Give me other  number")

if int(number_b) > int(number_a):
    print(f"the number {number_b} is grander than number {number_a}")

elif int(number_b) < int(number_a):
    print(f"the number {number_b} is less than number {number_a}")

else:
    print(f"the number {number_b} is equal to the number {number_a}")

"""""

"""""
note=input("What's your score?")

if int(note) >= 80 and int(note) < 101:
    print("your note is A")

elif int(note) >= 70 and  int(note) < 80 :
    print("your note is B")

elif int(note) >= 60 and  int(note) < 70 :
    print("your note is C")

elif int(note) >= 50 and  int(note) < 60 :
    print("your note is D")

elif int(note) >= 40 and  int(note) < 50 :
    print("your note is E")

else:
    print("There's a error")
"""""

"""""
input("What's the season")
season =input("Well What's the month?  ")

if season == "September" or  season == "October" or season == "November":
    print("The season is Autumn")
elif season == "December" or season == "January" or season == "February":
    print("The season is Winter")
elif season == "March" or season == "April" or season == "May":
    print("The season is Spring")
elif season == "June" or season == "July" or season == "August":
    print("The season is Summer")
else:
    print("That season doesn't exist")
"""""

"""""
fruits = ['banana', 'orange', 'mango', 'lemon']



fruit =input("Give me a fruit  ")

if fruit  != fruits[0] and fruit  != fruits[1] and fruit  != fruits[2] and fruit  != fruits[3]:
    fruits.append(fruit)
    print(fruits)
    print("That's a good fruit")

else:
    print("That fruit already exist in the list")
"""""


person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
"""""
print(person.keys())
#person.get("skills")
#print(person.get("user"))

#person.get("skills")
if "skills" in person.keys() :
    print(len(person['skills']))
    print(person['skills'][2])
    
else:
    print("This item doesn't exist my friend")


if "skills" in person.keys() :
    if "Python" in person['skills']:
        print(person['skills'][4])

else:
    print("That item doesn't exist")

front_end=["JavaScript" , "React"]
back_end =["Node", "Python", "MongoDB"]
skill_one = input("What tecnologi do you use?  ")
skill_two = input("What else?  ")


if skill_one in front_end and skill_two in front_end:
    print("you are a front end Developer")

elif skill_one in back_end and skill_two in back_end :
        print("you are a back end Developer")
else:
     print("You are other kind of developer")
"""""


if person['is_marred'] == True:
     if person['country'] == "Finland":
        print(person['first_name']," ", person['last_name']," lives in ",person['country'],"."," He is marred")
else:
     print(person['first_name'], person['last_name']," doesn't live in ",person['country'],"."," He is not merred")
