#If-elif-else
a = input("Enter a:")
b = input("Enter b:")
if (a==b):
    print("Equality")
elif (a>b):
    print("a is greater than b")
else:
    print("b is greater than a")

#eligibilty for license
#if-else statement
age = int(input("Enter age:"))
if (age>=18):
    print("Eligible")
else:
    print("Not Eligible")

#if statement
if(True):
    print("ok")

#if-elif statement
light =input("Enter value:")
if(light=="red"):
    print("Stop")
elif(light=="green"):
    print("go")
elif(light=="yellow"):
    print("look")

#if statement will be checked everytime it is in/present the code
num1 =5
if(num1>2):
    print("greater than 2")
if(num1>3):
    print("greater than 3")
#in the above code both the 'if statements' will be executed as if statement is checked everytime

#whereas elif staement is checked only if the 'if statement' is false 
#if the 'if statement is true than all the statements other than if will not be checked
num = 4
if(num>2):
    print("Greater than 2")
elif(num>3):
    print("Greater than 3")

#Grading System
Marks = int(input("Enter your marks:"))
if(Marks>=90):
    print("Your grade is A+")
elif(Marks>=80 and Marks<90):
    print("Your grade is A")
elif(Marks>=70 and Marks<80):
    print("Your grade is B+")
elif(Marks>=60 and Marks<70):
    print("Your grade is B")
elif(Marks>=50 and Marks<60):
    print("Your grade is C+")
elif(Marks>=40 and Marks<30):
    print("Your grade is D+")
elif(Marks>=30 and Marks<40):
    print("Your grade is D")
else:
    print("You did not qualify")


#Nesting
#here we nested if-else in if-else
age = 34
if(age>=18):
    if(age>=80):
        print("can't drive")
    else:
        print("can drive")
else:
    print("can't drive")