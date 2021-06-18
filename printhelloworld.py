# python basics
""" coments in python"""
'''comments'''

# print statement method 1

print("Welcome To Python")

# print statement method 2 using ASCII values

ascii = [87, 101, 108, 99, 111, 109, 101, 32,
         84, 111, 32, 80, 121, 116, 104, 111, 110]
for n in ascii:
    print(chr(n), end='')

print("\n")

# print statement using for loop
text = "Welcome To Python"

for x in text:

    print(x, end='')
