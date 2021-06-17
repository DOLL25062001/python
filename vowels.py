# to print each number of vowel present
"""
x = input("enter:")
print(x.count("a"))
print(x.count("e"))
print(x.count("i"))
print(x.count("o"))
print(x.count("u"))"""


# to print total vowels in a statement
"""
x=input()
a=x.count("a")
b=x.count("e")
c=x.count("i")
d=x.count("o")
k=x.count("u")
print(a+b+c+d+k)"""

"""
str=input()
vowels=0
for k in str:
     if(k=="a" or k=="e" or k=="i" or k=="o" or k=="u"):
       vowels=vowels+1
print(vowels) 

"""
x = input()
total = 0
vowel_list = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

for character in x:
    if character in vowel_list:
        total += 1
print(total)
