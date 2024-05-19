### Conditionales ###

#what're conditionales? Well, conditionals are part of encoding, this makes something in our coding work or not

my_conditional =1

#if my_conditional ==True: here we can see, this way to made a conditional is same than the next one 
#if my_conditional ==11: ##this this is False, cause 10 (5*2 =10) is not 11

if my_conditional ==10: ##this ###this is True, cause 10 (5*2 =10) is 10 
    print("Se ejecuta la condicion")
 ## here's a order because first working if, second elif and third else 
elif my_conditional >10 and my_conditional <20: # if needs a conditional
    print ("it's mayor than 10 and it's minus than 20") #the sentense is in the if
elif my_conditional == 1: ##elif needs a conditional
    print("it's 1")
else: ## else doesn't need a conditional 
    print("it't minus or equal than 10 or it's mayor than 20")
##all of the items are out from the else or if show it even thoug the conditional is true or false  
#print("it't minus or equal than 10 or it's mayor than 20") #The sentense is out from the else 
#print("it't minus or equal than 10 or it's mayor than 20")
#print("La ejecucion sigue")
### "Elif" isolates the conditions and causes only the actions in that part of the code to be executed

my_string ="" #when my string is empty this is False, cause there,s nothing in our val 
print(my_string)

if my_string:
    print("the condition works")

else:
    print("the condition doesn't work")

###Part one####
my_string ="My string  my friend" #when my string isn't empty this is true, cause there,s enything in our val 
print(my_string)

if my_string:
    print("my string is not empty")

else:
    print("the condition doesn't work")
####Part two###
if not my_string:
    print("my string is empty")

else:
    print("my string is not empty")

