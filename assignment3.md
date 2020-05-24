# Day-3
### You are given with a list of integer elements. Make a new list which will store square of elements of previous list
```
l=[]
n=int(input("enter the number of elements in list"))
for i in range(n):
    n1=int(input("enter the list element:"))
    l.append(n1)
a=[i*i for i in l]
print(a)
```
### From a list containing ints, strings and floats, make three lists to store them separately.
```
a=[1,"bye",2.02,"hi",3,347.27,54]
i=[]
s=[]
f=[]
for j in a:
    if type(j)==int:
        i.append(j)
    elif type(j)==str:
        s.append(j)
    elif type(j)==float:
        f.append(j)
print(i,s,f)
```

###3.	Print the pattern
```
1
1 2 
1 2 3
1 2 3 4
1 2 3 4 5
```

```
def tri(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()
n=int(input("Enter the number: "))
tri(n)
```    

### Accept data in two 3*3  matrix and calculate the sum of the matrices.
```
```

### Write a Python program to check whether a given number is a narcissistic number or not.i.e Armstrong Number
*For example, 371 is a narcissistic number,it has three digits, and if we cube each digits sum is 371. 
There are also 4-digit narcissistic numbers, some of which are 1634, 8208, 9474 since

```
def Nar_Arm(n):
    c=n
    sum1=0
    d=0
    r=[]
    while c>0:
        r.append(c%10)
        c=c//10
        d+=1
    sum1=sum([i**d for i in r])
    if sum1==n:
        return "Its an armstrong Number"
    else:
        return "Not a armstrong number"
n=int(input("Enter the number"))
print(Nar_Arm(n))
```
