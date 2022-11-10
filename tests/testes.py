user_name = input('enter your name:  ')

my_name = 'Rui'

str_statement = "Hello {}. My name is {}."

str_statement = str_statement.format(user_name, my_name)

print(str_statement)

#print(str_statement.__class__)

user_age = input('enter your age:  ')

print("you have lived for " + str(int(user_age)*12) + " months.")

