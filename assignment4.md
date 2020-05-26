# Day-4
### Write a function to find max of three numbers.
```
def max1(a,b,c):
    if a>b:
        if a>c:
            return a
        else:
            return c
    else:
        if b>c:
            return b
        else:
            return c
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=int(input("Enter the third number: "))
print(max1(a,b,c))
```

```
def max1(a,b,c):
    d=[a,b,c]
    return max(d)
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=int(input("Enter the third number: "))
print(max1(a,b,c))
 ```
 
### Write a Python program to detect the number of local variables declared in a function.

```
def max1():
    a=b=c=0
print(max1.__code__.co_nlocals)                    #3
```

###	Write a recursive function to calculate the sum of numbers from 0 to 10
* Expected output: 55	
```
def sum1(n):
    if n==1:
        return 1
    else:
        return n+sum1(n-1)
n=int(input("Enter the number: "))
print(sum1(n))
```  
### Create a function showStudent() in such a way that it should accept student id, name, and it’s college name  and if the id and college name is missing in function call it should show it as by default id is 1 and college name  is VITA.

```
def showStudent(name,Student_id=1,college_name="VITA"):
    print("Student Id:",Student_id)
    print("Name:",name)
    print("College:",college_name)
showStudent("Mic")
showStudent("ben",23)
showStudent("Tay",22,"CDAC")
```
     
### Write a Python function that takes a list and returns a new list with unique elements of the first list.

```
Sample List : [11,22,22,33,33,33,44,55,55,66]
Unique List : [11, 22,33, 44, 55,66]
```

```
a=[]
n=int(input("Enter the number of elements"))
for i in range(n):
    n1=int(input("enter list elements"))
    a.append(n1)
a=list(set(a))
a.sort()
print(a)
```
     
### Write a program to obtain the sum of the first and last digit of this number user defined functions
```
Example:
 Input:  5424
Output: 9
```

```
def sum1(n):
    a=[]
    while n>0:
        a.append(n%10)
        n=n//10
    return a[0]+a[-1]
n=int(input("Enter the number: "))
print(sum1(n))
```


