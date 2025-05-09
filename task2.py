#Task 2: Create a Personalized Greeting
#taking two variables firstName and secondName
#using "input" function for taking input from users

firstName = input('Enter your first name: ')
secondName = input('Enter your second name: ')

#here taking "fulName" as variable and performing concatenation
#for concatenation we are using '+' operator

fulName = firstName + ' ' + secondName + '!'
print("hello,",fulName,"Welcome to the python program.")