'''Python has built-in string validation methods for basic data. It can check if a string is composed of alphabetical characters, alphanumeric characters, digits, etc.

str.isalnum()
This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).

>>> print 'ab123'.isalnum()
True
>>> print 'ab123#'.isalnum()
False

str.isalpha()
This method checks if all the characters of a string are alphabetical (a-z and A-Z).

>>> print 'abcD'.isalpha()
True
>>> print 'abcd1'.isalpha()
False

str.isdigit()
This method checks if all the characters of a string are digits (0-9).

>>> print '1234'.isdigit()
True
>>> print '123edsd'.isdigit()
False

str.islower()
This method checks if all the characters of a string are lowercase characters (a-z).

>>> print 'abcd123#'.islower()
True
>>> print 'Abcd123#'.islower()
False

str.isupper()
This method checks if all the characters of a string are uppercase characters (A-Z).

>>> print 'ABCD123#'.isupper()
True
>>> print 'Abcd123#'.isupper()
False

Task

You are given a string
.
Your task is to find out if the string

contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

Input Format

A single line containing a string

.

Constraints

Output Format

In the first line, print True if
has any alphanumeric characters. Otherwise, print False.
In the second line, print True if has any alphabetical characters. Otherwise, print False.
In the third line, print True if has any digits. Otherwise, print False.
In the fourth line, print True if has any lowercase characters. Otherwise, print False.
In the fifth line, print True if has any uppercase characters. Otherwise, print False.'''

if __name__ == '__main__':
    s = input()
    flag1=0
    flag2=0
    flag3=0
    flag4=0
    flag5=0
    for i in range(len(s)):
        if s[i].isalnum():
            flag1=1
        if s[i].isalpha():
            flag2=1
        if s[i].isdigit():
            flag3=1
        if s[i].islower():
            flag4=1
        if s[i].isupper():
            flag5=1     
            
    if flag1==1:
        print("True")
    else:
        print("False")
    
    if flag2==1:
        print("True")
    else:
        print("False")
    
    if flag3==1:
        print("True")
    else:
        print("False")
    
    if flag4==1:
        print("True")
    else:
        print("False")
        
    if flag5==1:
        print("True")
    else:
        print("False")
    
