# Day-2
### Python Program to Read a Number n And Print the Series “1+2+…..+n= “
* sample:
```
Case 1:
Enter a number: 4
1 + 2 + 3 + 4 = 10 
Case 2:
Enter a number: 5
1 + 2 + 3 + 4 + 5 = 15
```

```
n=int(input("Enter the number of elements in series"))
l=[i for i in range(1,n+1)]
for i in l:
    if i==n:
        print(i,end="=")
    else:
        print(i,end="+")
print(sum(l))
```

### Write a Python program to count the number of even and odd numbers from a series of numbers.
```
Sample numbers :
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Output :
Number of even numbers : 4
Number of odd numbers : 5
```

```
def countodev(l):
    o=e=0
    for i in l:
        while i>1:
            i=i%2
        if i==0:
            e+=1
        else:
            o+=1
    print("Number of even numbers: ",e)
    print("Number of even numbers: ",o)
l=[]
n=int(input("Enter the number of elements: "))
for i in range(n):
    n1=int(input("Enter the elements: "))
    l.append(n1)
countodev(l)
```

### Write a Python program to create the multiplication table (from 1 to 10) of a number.
```
def table(n):
    for i in range(1,11):
        print('%d x %d = %d' % (n,i,n*i))
n=int(input("Enter the number of elements: "))
table(n)
```
### Given the triangle of consecutive odd numbers. Calculate Sum row wise.

![image](https://user-images.githubusercontent.com/63589909/82749269-a294cb80-9dc5-11ea-9335-f2ef92845778.png)

```
Example we call function :- row_sum_odd_numbers(2)
Result will be=3 + 5 = 8
if user give 4 then ur output is 13 + 15 + 17+ 19 = 64
```
```
def cons_tri_rowsum(n):
    return(n**3)                              #n*n*n
n=int(input("Enter the row number to get the sum: "))
print(cons_tri_rowsum(n))
```

### Write python program to print the pattern given below
* Note: Take input from user
```
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
```

```
def tri(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(i,end="")
        print()
n=int(input("Enter the number: "))
tri(n)
```
