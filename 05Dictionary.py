dog = dict()
dog ={"Name","Color","breed","legs","age"}
print(dog)
print(type(dog))

student ={"first_name":"Fabi","last_name":"Castro","gender":"fgfdg","age":"18","marital":"single","skills":["Drawing","runing","waiting"],"country":"Mexico","city":"Monterrey","address":"Pino de arizona"}
print(type(student))
print(student)
print(len(student))

print(student["skills"])
print(type(student["skills"]))

student["skills"]=["listening","speaking","writing"]
print(student)
print(list(student.keys()))
print(list(student.values()))
print(list(student.items()))
print(tuple(student.items()))
del student["skills"]
print(student)

student.pop("first_name")
print(student)
del student
print(student)