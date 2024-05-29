#### Loops ###
#The loop works to repeat a part  of code

#While 

my_condition=0

while my_condition < 10: #This  is a if but a if with repeat my friend 
    print(my_condition)

    my_condition += 2 #Sentinel
#if my_condition==10:
    #print ("My condition is equal to 10") #in this part of code we use a if but the else is not its the esle belongs While, that's way that print in the console jdjd


#elif my_condition=10: The elif can't use 
#print() 
else:  #Else is optinal 
    print("My condition is mayor than 10") #In python you can use the else, cause the While is like a If but with repeat fjkdjfk


print("the print works wow")

while my_condition < 20:

    my_condition += 1

    if my_condition==15:#You can make a loop meet one condition and you can also make it stop depending on another condition
        print("Execution stops")
        break #if there's eny conditional very specific and you need to stop the program, you can use Break 
    print(my_condition)  

#print("My condition is minus than 20")

#another loop --> "FOR" has meet a condition but also it most repeat a list of objects 

# in this part you can see, for should be repeated depending on how many elemnts we have in dataset

my_list_one = [35,24,62,52,30,30,17]

for element in my_list_one: #The "For" should be repeated depending on how many elements we have in a dataset
    print(element)


my_tuple=(35,1.50,"Fabi","Castro","Castro")
for element in my_tuple:
    print(element)

my_set= {"Fabi","Castro",18}

for element in my_set:
    print(element)



ny_dict ={"Name":"Fabi","Last Name":"Castro","Age":18, 1:"p"}

for element in ny_dict:
    print(element)
    if element =="Age":
        print("Age is in My Dict")
        continue #"Continue" works to restart the "FOR", so the last line is ignored
        #break #here we've made the execution break when the key is "Age"
        
    print("it works")

else:
    print("The loop FOR for my dict is over")#This part of code doesn't show cause in the line 61 we breake the for

print("this works") #Why does this part work? well because the Brake Braks the For and its elements (if and else in this case)