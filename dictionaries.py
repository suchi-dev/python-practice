students = {}
print(type(students))
students = {"Alice" : 25, "Bob": 27, "Claire" : 17, "Dan" : 21, "Emma" : 22}
print(students["Alice"])
print(students["Dan"])
students["Fred"] = 25
print(students["Fred"])
students["Alice"] = 26
print(students["Alice"])
del students["Fred"]
## --key error print(students["Fred"])
print(students.keys())
a = list(students.keys())
print(a[0])
print(students.values())
b = list(students.values())
print(b[2])
print(students)
print(students["Dan"])