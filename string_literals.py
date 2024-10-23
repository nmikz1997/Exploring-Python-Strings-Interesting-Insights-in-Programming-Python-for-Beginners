#F-strings make string formatting more readable and convenient!

name = "Alice"
age = 30
greeting = f"My name is {name} and I am {age} years old."
print(greeting)

#dynamic dir

user = 'Alex'
dirToSee = fr'C:\Users\{user}\Downloads'
print (dirToSee) # prints C:\Users\Alex\Downloads