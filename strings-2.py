x = "happy birthday"
print(x.index("birthday"))
print(x.find("birthday"))
print(x.find("zalll"))
y = "00000000happy0000birthday000000"
print(y.strip("0"))
print(y.lstrip("0"))
print(y.rstrip("0"))

name = input("What is your name?: ")
print(name)
print(len(name))
formatted_name = input("What is your name?: ").strip()
print(formatted_name)
print(len(formatted_name))