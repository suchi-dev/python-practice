#Ask user for name
name = input("What is your name?: ")
print(type(name))
#Ask user for age
age = input("How old are you?: ")
print(type(age))
# Ask user for city
city = input("Where do you live?: ")
#Ask user what they enjoy
love = input("What do you love doing?:")
#Create output text
output = "Your name is {} and you are {} years old. You live in {} and you love {}"
formatted_text = output.format(name, age, city, love)
#Print output to screen
print(output)
print(formatted_text)