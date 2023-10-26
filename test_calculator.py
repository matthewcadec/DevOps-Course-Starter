def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter a second number: "))
sign = input("Please enter an expression: ")

if sign == '+':
    print(add(num1, num2))
if sign == '-':
    print(subtract(num1, num2))
if sign == '/':
    print(divide(num1, num2))
if sign == '*':
    print(multiply(num1, num2))