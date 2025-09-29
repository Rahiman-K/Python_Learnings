# operators

# Arithmetic operators
"""
Addition
subtraction
Multiplication
Division
Modulus
"""

# Conditional operators
"""
>, <, >=, <=, !=, ==, 
"""

# Logical Operators
"""
AND, OR, NOT
"""

# addition
print(2+3)

#subtraction
print(3-2)

#mutiplication
print(2*19)

#division
print(4/2)

#moduls
print(4%2)

# bit wise operators are AND, OR, NOT
x = int(input("Enter value for x "))
b = int(input("Enter value for b "))
print (not x) # for scenario if x is true not x gives false

if x > 2 and b < 4: # This statement is having both conditional operator and logical operators
    print("both statements are true")

if x > 2 or b < 10:
    print(f"any one value is true and value x is {x}, and value of b is {b}")