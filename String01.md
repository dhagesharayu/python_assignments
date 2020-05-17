# Python Data Type: String - Exercises-1
 
 
### Write a Python program to calculate the length of a string.
```
s=input("enter the string")
print("the length of the string is:",len(s))
s=input("enter the string")
```
```
c=0
for i in s:
    c+=1
print("the length of the string is:",c)
```
### Write a Python program to count the number of characters (character frequency) in a string.
```
Sample String : google.com'
Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
```
```
s=input("enter the string")
a={}
for i in s:
    if i in a:
        a[i]+=1
    else:
        a[i]=1
print(a)
```
### Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.
```
Sample String : 'w3resource'
Expected Result : 'w3ce'
Sample String : 'w3'
Expected Result : 'w3w3'
Sample String : ' w'
Expected Result : Empty String
```
```
s=input("enter the string")
if len(s)<2:
    print("")                                                                 #Empty String
else:
    print(s[:2]+s[len(s)-2:])
```
### Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
```
Sample String : 'restart'
Expected Result : 'resta$t'
```
```
s=input("enter the string")
a=list([s])                                                             #entire string in list
a=list(s)                                                               #string split up as alpha in list
print(a)
for i in range(1,len(a)):
    if a[i]==a[0]:
        a[i]="$"
b="".join(a)
print(b)
```
### Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
```
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'
```
```
s1=input("enter the first string")
s2=input("enter the second string")
a=list(s1)
b=list(s2)
a[0],b[0]=b[0],a[0]
a[1],b[1]=b[1],a[1]
print("".join(("".join(a))+" "+("".join(b))))
 ```
 
### Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
```
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'
```
```
s=input("enter the string")
a=list(s)
if len(s)<3:
    print(s)
else:
    if a[-3:len(a)]!="ing":
        b="".join(("".join(a))+"ing")
        
    else:
        b="".join(a+"ly")
    print(b)
```
### Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
```
Sample String : 'The lyrics is not that poor!'
'The lyrics is poor!'
Expected Result : 'The lyrics is good!'
'The lyrics is poor!'
 ```
 * find() function returns -1 if it is not found, else it returns first occurrence i.e position
```
s=input("enter the string")
l1=s.find("not")
l2=s.find("poor")
if l1!=-1 and l2!=-1 and l1<l2:
    s=s.replace(s[l1:l2+4],"good")
elif l1==-1 and l2!=-1:
    s=s.replace(s[l2:l2+4],"good")
print(s)
```
### Write a Python function that takes a list of words and returns the length of the longest one.
```
a=[]
while True:
    n=input("enter words in the list and 0 to stop")
    if n=="0":
        break
    a.append(n)
d={}
for i in a:
    d[i]=len(i)
m=max(d,key=d.get)                               #key that has max value
print(m)
m=max(d.values())                                #max value
``` 
 
### Write a Python program to remove the nth index character from a nonempty string.
```
s=input("enter the string")
n=int(input("enter the index from which you want to remove the char"))
s=s.replace(s[n],"")                                   #same char in diff index also deleted
print(s)

print(s[:n]+s[n+1:])                                   #only index value deleted
``` 
### Write a Python program to change a given string to a new string where the first and last chars have been exchanged.
```
s=input("enter the string")
s=list(s)
s[0],s[-1]=s[-1],s[0]
print("".join(s))

print(s[-1]+s[1:len(s)-1]+s[0])
 ```
 
### Write a Python program to remove the characters which have odd index values of a given string.
```
s=input("enter the string")
print(s[0::2])
s=input("enter the string")
s=s[0::2]
print(s)
```
### Write a Python program to count the occurrences of each word in a given sentence.
```
s=input("enter the string")
a=s.split()                                                                     #a=s.split(" ")  " " is default
d={}
for i in a:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)
```
### Write a Python script that takes input from the user and displays that input back in upper and lower cases.
```
s=input("enter the string")
print("uppercase:",s.upper())
print("lowercase:",s.lower())
```
### Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically).
```
Sample Words : red, white, black, red, green, black
Expected Result : black, green, red, white,red
```
```
s=input("enter the string")
a=s.split(",")
a.sort()
print(",".join(a))
```
### Write a Python function to create the HTML string with tags around the word(s).
```
Sample function and result :
add_tags('i', 'Python') -> '<i>Python</i>'
add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'
```
```
s=input("enter the string")
t=input("enter the tag")
a="<"+t+">"+s+"</"+t+">"
print(a)
```
### Write a Python function to insert a string in the middle of a string.
```
Sample function and result :
insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
insert_sting_middle('{{}}', 'PHP') -> {{PHP}}
```
```
s1=input("enter the first string")
s2=input("enter the second string to be inserted in middle")
l=int(len(s1)/2)
s1=s1[:l]+s2+s1[l:]
print(s1)
```
### Write a Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2).
```
Sample function and result :
insert_end('Python') -> onononon
insert_end('Exercises') -> eseseses
```
```
s=input("enter the string")
s1=""
if len(s)<2:
    print("Empty string")
else:
    for i in range(0,4):
        s1=s1+(s[-2:])
print(s1)
```
```
s=input("enter the string")
s1=""
if len(s)<2:
    print("Empty string")
else:
    s1=s1+(s[-2:]*4)
print(s1)
```
### Write a Python function to get a string made of its first three characters of a specified string. If the length of the string is less than 3 then return the original string.
```
Sample function and result :
first_three('ipy') -> ipy
first_three('python') -> pyt
```
```
def first_three(s):
    if len(s)<=3:
        return s
    else:
        return s[:3]
```
```
s=input("enter the string")
print(first_three(s))
```
### Write a Python program to get the last part of a string before a specified character.
```
https://www.w3resource.com/python-exercises
https://www.w3resource.com/python
```
* .rsplit() searches for the splitting string from the end of input string, and the second argument limits how many times it'll split to just once.
Another option is to use str.rpartition(), which will only ever split just once
```
s=input("enter the string")
n=input("enter the charc you want to split on")
a=s.rsplit(n,1)[0]
b=s.rpartition(n)[0]
print(a)
print(b)
```
### Write a Python function to reverses a string if it's length is a multiple of 4.
```
def reverse(s):
    n=len(s)
    while n>=4:
        n=n%4
    if n==0:
        return s[::-1]
    else:
        return s
s=input("enter a string multiple of 4 to be reversed")
print(reverse(s))
```
 
### Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.
```
def func(s):
    c=0
    a=s[:4]
    for i in a:                                                                        #for i in s[:4]:
        if i.isupper():
            c+=1
    if c>=2:
        return s.upper()
    else:
        return s
        
s=input("enter the string")
print(func(s))
```
### Write a Python program to sort a string lexicographically., i.e Alphabetic
```
def lexi(s):
    a=list(s)
    a.sort()
    return "".join(a)
        
s=input("enter the string")
print(lexi(s))
```
### Write a Python program to remove a newline in Python.
* rstrip() method removes all the trailing characters from the string. It means it removes all the specified characters from right side of the string. If we don't specify the parameter, It removes all the whitespaces from the string. This method returns a string value.
```
def remove_newline(s):
    return s.rstrip()                                                     #return s.rstrip("\\n")
        
s=input("enter the string")
print(remove_newline(s))
```
### Write a Python program to check whether a string starts with specified characters.
*Single Character
```
def check(s,c):
    if s[0:1]==c:
        return True
    else:
        return False

s=input("enter the string")
c=input("Enter the char to check")
print(check(s,c))
 ```
 * Multiple Characters       
```
def check(s,c):
    return s.startswith(c)
        
s=input("enter the string")
c=input("Enter the char to check")
print(check(s,c))
```
### Write a Python program to create a Caesar encryption.
* Note : In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence.
 To get the ASCII code of a character, use the ord() function. To get the character encoded by an ASCII code number, use the chr() function
```
def encryp(s,s1):
    a=list(s)
    b=""
    for i in a:
        if i.isupper():
            d=ord(i)
            if (d+s1)>90:
                d=65+(d+s1-90)
            else:
                d=d+s1
            b+=chr(d)
        elif i.islower():
            d=ord(i)
            if (d+s1)>122:
                d=97+(d+s1-122)
            else:
                d=d+s1
            b+=chr(d)
    return b
s=input("enter the string")
s1=int(input("Enter the step for encryption"))
print(encryp(s,s1))
```
### Write a Python program to display formatted text (width=50) as output.
```
import textwrap
def form(s,s1):
    return textwrap.fill(s,width=s1)
    
s=input("enter the string")
s1=int(input("Enter the width for format"))
print(form(s,s1))
```
### Write a Python program to remove existing indentation from all of the lines in a given text.
```
import textwrap
def removeindent(s):
    return textwrap.dedent(s)
    
s=input("enter the string")
print(removeindent(s)
```
### Write a Python program to add a prefix text to all of the lines in a string.
```
import textwrap
def prefix(s,s1):
    s= textwrap.fill(s,width=s1)
    return textwrap.indent(s,"* ")
    
s=input("enter the string")
s1=int(input("Enter the width to wrap"))
print(prefix(s,s1))
```
### Write a Python program to set the indentation of the first line.
```
import textwrap
def setin(s,a):
    s=textwrap.dedent(s).strip()
    return textwrap.fill(s,initial_indent=" ",subsequent_indent=" "*4,width=a)
s=input("Enter the text:  ")
a=int(input("Enter the width:  "))
print(setin(s,a))
```
### Write a Python program to print the following floating numbers upto 2 decimal places.
```
def form(s):
   return "{:.2f}".format(s)
s=float(input("Enter the number"))
print(form(s))
```
### Write a Python program to print the following floating numbers upto 2 decimal places with a sign.
```
def form(s):
   return "{:+.2f}".format(s)
s=float(input("Enter the number"))
print(form(s))
```
### Write a Python program to print the following floating numbers with no decimal places.
```
def form(s):
   return "{:.0f}".format(s)
s=float(input("Enter the number"))
print(form(s))
```
### Write a Python program to print the following integers with zeros on the left of specified width.
```
def form(n):
   return "{:0>6d}".format(n)
n=int(input("Enter the number"))
print(form(n))
```
### rite a Python program to print the following integers with '*' on the right of specified width.
```
def form(n):
   return "{:*<6d}".format(n)
n=int(input("Enter the number"))
print(form(n))
```
### Write a Python program to display a number with a comma separator.
```
def form(n):
   return "{:,}".format(n)
n=int(input("Enter the number"))
print(form(n))
```
### Write a Python program to format a number with a percentage.
```
def form(n):
   return "{:.2%}".format(n)
n=float(input("Enter the number"))
print(form(n))
```
### Write a Python program to display a number in left, right and center aligned of width 10.
```
def form(n):
    print("{:<10d}".format(n))
    print("{:^10d}".format(n))
    print("{:>10d}".format(n))
n=int(input("Enter the number"))
form(n)
```
### Write a Python program to count occurrences of a substring in a string.
 ```
 def cnt(s,s1):
    return s.count(s1)
   
s=input("Enter the String")
s1=input("Enter the substring")
print(s1,"ocurs in",s,cnt(s,s1),"times")
```
```
def cnt(s,s1):
    a=len(s1)
    c=0
    for i in range(len(s)):
        if s[i:i+a]==s1:
            c+=1
    return c
s=input("Enter the String")
s1=input("Enter the substring")
print(s1,"ocurs in",s,cnt(s,s1),"times")
```
### Write a Python program to reverse a string.
```
def rev(s):
    a=list(s)
    a.reverse()
    return "".join(a)
s=input("Enter the String to be reversed")
print(rev(s))
```
```
def rev(s):
    return "".join(reversed(s))
s=input("Enter the String to be reversed")
print(rev(s))
```

### Write a Python program to reverse words in a string.
```
def rev(s):
    s=s.split()
    a=[]
    for i in s:
        a.append("".join(reversed(i)))
    return " ".join(a)
s=input("Enter the String for words to be reversed")
print(rev(s))
```
```
def rev(s):
    s=s.split()
    s=s[::-1]
    return " ".join(s)
s=input("Enter the String for words to be reversed")
print(rev(s))
```
```
def rev(s):
    return " ".join(s.split()[::-1])
s=input("Enter the String for words to be reversed")
print(rev(s))

```

### Write a Python program to strip a set of characters from a string.
```
def removechar(s,sub):
    for a in s:
        if a in sub:
            s=s.replace(a,"")
    return s
   
s=input("Enter the String")
sub=input("Enter the characters to be removed from string")
print(removechar(s,sub))
```
```
def removechar(s,sub):
    return "".join([i for i in s if i not in sub])
   
s=input("Enter the String")
sub=input("Enter the characters to be removed from string")
print(removechar(s,sub))
```
### Write a Python program to count repeated characters in a string.
```
Sample string: 'thequickbrownfoxjumpsoverthelazydog'
Expected output :
o 4
e 3
u 2
h 2
r 2
t 2
```

```
 def cnt(s):
    d={}
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    d=sorted(d.items(),key=lambda x:x[1],reverse=True)
    for i in d:
        if i[1]>1:
            print(i[0],i[1])
        
s=input("Enter the String to count the characters")
cnt(s)

```
```
import collections
def cnt(s):
    d=collections.defaultdict(int)
    for i in s:
        d[i]+=1
    for b in sorted(d,key=d.get,reverse=True):
        if d[b]>1:
            print("%s %d"%(b,d[b]))

s=input("Enter the String to count the characters")
cnt(s)

```



