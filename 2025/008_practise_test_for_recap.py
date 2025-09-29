# Practise Test 1

"""
Q1 : program that is used to print simple statement as below

Hello, World! Welcome to Python
"""
print("Hello, World! Welcome to Python")

"""
Q2: print statements like below

Twinkle, twinkle, little start, 
How I wonder what you are!
"""
print("\n") # just to a new line

print("Twinkle, twinkle little start,\nHow I wonder what you are!")

"""
Q3: Create variable to store - your name 
your age
your height in meter 
a boolean value representing whether you are student
"""

name = 'Rahiman'
age = 26
height = 1.76
print(name)
print(age)
print(height)

"""
Q4: Typecast num = '45' to integer and add 10 to it and print the result
"""
num = "45"
value = int(num) + 10
print(value)

"""
Q5: ask user for their favorite food and print it
"""
food = input("Favorite Food")
print(f"Wow! I also like {food}")

"""
Q6: Take two numbers as input from the user
print their sum, difference, product and division
"""

a = int(input("Enter number1 : "))
b = int(input("Enter number2 : "))
print("Sum ",a+b)
print("difference",a-b)
print("multiplication", a*b)
print("division", a/b)

"""
Q7: Escape sequences
Print the following

Harry said, "Python is awesome!"
This is on a new line.
This is a tab here
"""

print('Harry said, "Python is awesome!\nThis is on a new line\nThis is a tab \t here')

"""
Q8: Operator Challenge
take input and print square and cube of that number 
"""
x = int(input("Enter number : "))
print("Square of number is ",x^2)
print("Cube of number is ",x^3)

