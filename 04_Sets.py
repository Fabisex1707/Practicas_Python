### Exercise sets ### 

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
it_companies.add("Twitter")
print(it_companies)
it_companies=it_companies.union({"CodeClean","Contentsquare","Enigma"})
print(it_companies)
print(type(it_companies))

it_companies.remove("CodeClean")
print(it_companies)
it_companies.discard("Enigma") # the diffrence between remove nad discard is, discar just doesn't show the item but don't delete and the remove() deletes te item 
print(it_companies)

print(it_companies)

#print(it_companies.union({"CodeClean","Contentsquare","Enigma"}))

### Exercises: Level 2 ###
print(A.union(B))
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
print(A.union(B).union(A))
print(A.symmetric_difference(B))
del it_companies,A,B
#print(it_companies)
#print(A)
#print(B)

### Exercises: Level 3 ###

print(len(age))

age=set(age)
print(type(age))

print(len(age))
print(age)

# string: thsi type of data admit only characters an strings of characters 
#list: this type of data admits a Dataset and it's mutable
#tuple: this type of data admits a Dataset and it's not mutable
#set: this type of data admits a Dataset but doesn't admits repeated things and there's not a order for the Dataset

tense=set()
tense={"I","am","a","teacher","and","I","love","to","inspire","and","teach","people"}
print(tense)
print(len(tense))

