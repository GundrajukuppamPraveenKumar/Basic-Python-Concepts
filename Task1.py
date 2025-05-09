#Module 2: Basic Python Concepts
#Task 1: Perform Basic Mathematical Operations

# first take two variable firstNumber and secondNumber
#use "input" function for taking inputs from user
firstNumber = input("Enter your first number: ")
secondNumber = input("Enter your second number: ")

#basically inputs in string type
#for converting string to integer we here used "int" function

firstNumber = int(firstNumber)
secondNumber = int(secondNumber)

#Performs the basic mathematical operations on  two numbers
#taking variables add,sub,mul,div
#writing relevant logic and assigning wise vera
#here operands are firstNumber,secondNumber
#operators are +,-,*,/
add = firstNumber + secondNumber
sub = firstNumber - secondNumber
mul = firstNumber * secondNumber
div = firstNumber / secondNumber

#using "print" function for printing output values
print('Addition:', add)
print('Subtraction:', sub)
print('Multiplication:', mul)
print('Division:', div)
