'''
Write a Python program to add 'ing' at the end of a given string (length
should be at least 3). If the given string already ends with 'ing' then add
'ly' instead if the string length of the given string is less than 3, leave it
unchanged.
'''
a=input("Enter string:")
if len(a)>=3:
    if a[-3:]=="ing":
        a += "ly"
        print(a)
    else:
        a +="ing"
print(a)

