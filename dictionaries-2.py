students = {"Alice": 26, "Bob": 27, "Claire": 17, "Dan": 21, "Emma": 22}

my_students = {"Alice": ["ID001", 26, "A"],
               "Bob": ["ID002", 27, "B"],
               "Claire": ["ID003", 17, "C"],
               "Dan": ["ID004", 21, "D"],
               "Emma": ["ID005", 22, "E"]}

print(my_students["Claire"])
print(my_students["Claire"][0])
print(my_students["Dan"][1:])

my_students_dict = {"Alice": {"id" : "ID001", "age": 26, "grade" : "A"},
                    "Bob": {"id": "ID002", "age": 27, "grade": "B"},
                    "Claire": {"id": "ID003", "age": 17, "grade": "C"},
                    "Dan": {"id": "ID004", "age": 21, "grade": "D"},
                    "Emma": {"id": "ID005", "age": 22, "grade": "E"}}
print(my_students_dict["Dan"]["age"])
print(my_students_dict["Emma"]["id"], my_students_dict["Emma"]["grade"])
