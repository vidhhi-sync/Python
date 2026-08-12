#strings

str1= "this is a string"
str2 = 'this is also a string'
str3= """this is also an example of string"""

s="This is a string. we are creating it in a python"
print(s)
#now we want to print the above string in two different line so we will use escape sequence characters
s="This is a string. \n we are creating it in a python"
print(s)
#to give space between texts we use tab (\t)
s="This is a string.\t we are creating it in a python"
print(s)

#Basic Operations on strings

#Concatenation
s1 = "Welcome!"
s2 = " Vidhi"
s3 = s1+s2
print(s3)

#Finding length of a string using len() function
str= "This is a string"
print(len(str)) 
#in length function the space between string is also calculated as length.

#Indexing
st = "Vidhi Bansal"
print(st[2])

#Slicing
strr= "Vidhi"
print(strr[0:5])
print(strr[0:4])

#printing full string in one go
print(strr[0:]) #[0:5] or [0:len(strr)]
ss= strr[0:len(strr)]
print(ss)

#printing from start to a particular index number
print(strr[:4]) #[0:4]
print(strr[0:4])

#Negative Indexing in slicing
string = "Apple"
print(string[-5:-2])

#String Functions

#str.endswith()
#this function checks whether our string ends with something particular or not
b = "I am Vidhi Bansal."
print(b.endswith(" Bansal."))

#str.capitalize()
#This function capitalize the first letter of the string
a = "hi"
print(a.capitalize())
#this function works only once , it doesn't change the original string
print(a)
#but if we want to change in original string then we can store it in another variable
c = a.capitalize() #now this changes in original string
print(c)

#str.replace(old,new)
#this function is used to replace any specific value to another value
d = "this is a string"
print(d.replace("i","e"))

#str.find(word)
#this function helps in finding a word in a string
#if the word is present in string then the occurence of that word 1st time prints 1st index number of that word
e = "This is a string function"
print(e.find("a"))
print(e.find("x")) #here it gives negative as it doesn't include in that string so considered invalid

#str.counts()
#this function helps in counting the number of occurence of that word in a string
f = "Hi this is vidhi"
print(f.count("i"))
print(f.count("h"))
print(f.count("m"))

