# all about the string representation

# Ask user for their name
name = input('What s your name? ')

name = input('what s your name?').strip().title()


# remove whitespace from str
name = name.strip()

name= name.strip().title()

# split user s name into first name last name
first = name.split(" ")

# Capitalize user s name
name = name.capitalize()

name = name.title()
# say hello to user
print(name)
print('hello, name')
print('hello', name)
print('hello' + name) # 
print('hello,', sep=" ")
print('hello,', end=" ")

print(f"hello, {name}")

# how should has aspas 
print('hello, "friend" ')
print("hello, \"friend\"")


# all about this int python function
# + - * / %
# interactive mode
# calculator
x = int(input('What s x? '))
y = int(input('What s y? '))
#z = int(x) + int(y)
print(x + y)

#float 

z = float(input('What z? '))
c = float(input('What c? '))
f = round(z + c)
a = round(z / c, 2)
print(f)
print(f'{f:,}')