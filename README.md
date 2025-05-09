# Basic-Python-Concepts
ASSIGNMENT 1
##Task 1: Perform Basic Mathematical Operations
Problem Statement: Write a Python program that does the following:
1.  Takes two numbers as input from the user.
2.  Performs the basic mathematical operations on these two numbers:
o	Addition
o	Subtraction
o	Multiplication
o	Division
3.  Displays the results of each operation on the screen.
 Expected Output:
The output should include the result of each operation performed, for example:
 
Enter your first number: 5
Enter your second number: 10
Addition: 15
Subtraction: -5
Multiplication: 50
Division: 0.5

Solution:-
 first take two variable firstNumber and secondNumber
use "input" function for taking inputs from user
firstNumber = input("Enter your first number: ")
secondNumber = input("Enter your second number: ")

basically inputs in string type
for converting string to integer we here used "int" function

firstNumber = int(firstNumber)
secondNumber = int(secondNumber)

Performs the basic mathematical operations on  two numbers
taking variables add,sub,mul,div
writing relevant logic and assigning wise vera
here operands are firstNumber,secondNumber
operators are +,-,*,/
add = firstNumber + secondNumber
sub = firstNumber - secondNumber
mul = firstNumber * secondNumber
div = firstNumber / secondNumber

using "print" function for printing output values
print('Addition:', add)
print('Subtraction:', sub)
print('Multiplication:', mul)
print('Division:', div)

Task 2: Create a Personalized Greeting
Problem Statement: Write a Python program that:
1.  Takes a user's first name and last name as input.
2.  Concatenates the first name and last name into a full name.
3.  Prints a personalized greeting message using the full name.
Expected Output:
The program should output a greeting like:
Enter your first name: john
Enter your second name: doe
hello, john doe! Welcome to the python program.

solution:
Task 2: Create a Personalized Greeting
taking two variables firstName and secondName
using "input" function for taking input from users

firstName = input('Enter your first name: ')
secondName = input('Enter your second name: ')

here taking "fulName" as variable and performing concatenation
for concatenation we are using '+' operator

fulName = firstName + ' ' + secondName + '!'
print("hello,",fulName,"Welcome to the python program.")
