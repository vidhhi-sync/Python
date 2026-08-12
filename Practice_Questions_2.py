#practice

#Ques-1 Write a program to input user's first name and print it's length
str = input("Enter your name:")
print("My name is:",str)
print(len(str))

#Ques-2 Write a program to find the occurence of $ in string.
str1 = "The price ($) of the apple juice is: $0.2"
print(str1)
print(str1.count("$"))

#Ques-3 Write a program to check a number entered by user is odd or even.
num = int(input("Enter number:"))
if(num%2==0):
    print("even")
else:
    print("odd")

#Ques-4 Write a program to find greatest of 3 numbers entered by user
a = int(input("Enter value:"))
b = int(input("Enter value:"))
c = int(input("Enter value:"))
if (a>b and a>c):
    print("a is greatest")
elif(b>a and b>c):
     print("b is greatest")
elif(c>a and c>b):
    print("c is greatest")

#Ques-5 Write a program to check if a number is divisible by 7 or not
m = int(input("Enter value:"))
if(m%7==0):
    print("Divisor of 7")
else:
    print("Error")