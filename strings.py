name = "Suchitra"
print(type(name))
message = 'John said to me "I will see you later"'
print(message)

long_message="""Hello I am Suchitra.
I live in Pune and 
I work with Mastercard"""

print(long_message)
hello = "HelloWorld !"
print(hello)
a = "Part one"
b = "Part two"
#concat strings
print(a + " "+b)
print(a * 3)
print("="*20)
c = "part"
d = 1
e = c + str(d)
print(e)
print("{} - {}".format(c,d))
print("{1} : {0}".format(c,d))


print("Suchitra".count("a"))
text = "happy birthday"
print(text.count(("a")))
print(text.count("day"))

#convert sting to upper, lower case
x = "Happy Birthday"
print(x.lower())
print(x.upper())
y = "happy birthday"
print(y.capitalize())
x = x.upper()
print(x)
x = x.lower()
print(x)
print(x.title())
print(x.islower())
print(x.isupper())
print(x.isalpha())
print("abcd".isalpha())
print(x.isdigit())
print("123".isdigit())
z = "Happybirthday123"
print(z.isalnum())