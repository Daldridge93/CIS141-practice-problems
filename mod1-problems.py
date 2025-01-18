
'''1. Create a program that prints the following output to the screen:
"Water. Earth. Fire. Air. Long ago, the four
nations lived together in harmony. Then, everything changed when the Fire Nation attacked."'''

print("Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony. Then, everything changed when the Fire Nation attacked.")



'''2. Create a program that prompts for 2 numbers and then outputs the addition, subtraction, multiplication,
and division of the first number by the second number.'''


a = float(input("Please provide the first number: "))
b = float(input("Please provide the first number: "))

print("Addition: ",a + b)
print("Subtraction: ",a - b)
print("Multiplication: ",a * b)
print("Division: ",a / b)




'''3. Create a program that prompts for the side lengths of a
triangle and computes the area using Heron's formula.'''


import math
a = float(input("What is the length of the first side?"))
b = float(input("What is the length of the Second side?"))
c = float(input("What is the length of the third side?"))
s = (a + b + c ) / 2
A = float(math.sqrt(s * (s-a) * (s-b) * (s-c)))

print("The area of your triangle is:", A)





# problem number 4


a = float(input("Please provide the first number: "))
b = float(input("Please provide the Second number: "))
c = float(input("Please provide the Third number: "))
d = float(input("Please provide the fourth number: "))
e = float(input("Please provide the fifth number: "))
numbers = a,b,c,d,e
total = a + b + c + d + e
minimum = min(a,b,c,d,e)
maximum = max(a,b,c,d,e)
avg = (a + b + c + d + e) / 5
std1 = (a - avg)**2 + (b - avg)**2 + (c - avg)**2 + (d - avg)**2 + (e - avg)**2
std2 = (std1 / 5)
print("You entered the following numbers:",numbers)
print("Minimum:",minimum)
print("Maximum:",maximum)
print("Range:",maximum - minimum)
print("Average:",avg)
print("Total:",total)
print("Stnadard Deviation", math.sqrt(std2))
