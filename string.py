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