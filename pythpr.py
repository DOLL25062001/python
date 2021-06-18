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

# print a number ex:34 method1
x = "Hi you are reading a line to count"
print(len(x))

# method 2

print("34")

# method 3
number = 8
print(len("Hi you are reading a line ")+number)

# method 4 binary form  binary numbers are prefixed with 0b
print(0b100010)
