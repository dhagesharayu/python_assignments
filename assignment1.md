# Assignment 1
### Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).
  * The numbers obtained should be printed in a comma-separated sequence on a single line.
  * Hints: Consider use range(#begin, #end) method
```
for i in range(2000,3201):
    if (i/7)==(i//7) and (i/5)!=(i//5):
        print('%d,'%(i),end="")
```
### With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
```
  Suppose the following input is supplied to the program:
	8
	Then, the output should be:
	{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
```

* Hints: In case of input data being supplied to the question, it should be assumed to be a console input. Consider use dict()

```
n=int(input("Enter the number"))
d={}
for i in range(1,n+1):
    d[i]=i**2
print(d)
```
### Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
```
  Suppose the following input is supplied to the program:
	Hello world
	Practice makes perfect
	Then, the output should be:
	HELLO WORLD
	PRACTICE MAKES PERFECT
```

* Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

```
b=[]
while True:
    s=input("enter String and s to stop")
    if s=="s" or s=="S":
        break
    else:
        b.append(s.upper())
for i in b:
    print(i)
```
### Write a program to check whether number is even or odd using if Else statement…
```
def oddeven(n):
    c=n
    while c>1:
        c=c%2
    if c==0:
        print('%d is a even number'%(n))
    else:
        print('%d is a odd number'%(n))
n=int(input("Enter number to check odd even"))
oddeven(n)
```
### program that grants access only to kids aged between 8-12 using  if  else statement
* Hint: If aged between 8 to 12 then you are allowed… welcome!!, otherwise Sorry not allowed ..Bye!
```
def entry(n):
    if n>=8 and n<=12:
        print("you are allowed… welcome!!")
    else:
        print("Sorry not allowed ..Bye!")
n=int(input("Enter the age"))
entry(n)
```

