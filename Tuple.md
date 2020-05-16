# Python Data Types: Tuple - Exercises
 
### Write a Python program to create a tuple.
```
a=(1,2)
b=tuple()
print(a,type(a))           #(1, 2) <class 'tuple'>
print(b,type(b))           #() <class 'tuple'>
```
### Write a Python program to create a tuple with different data types.
```
a=[1,2]
b="suig"
i=1
j=1.3
t=(a,b,i,j,True,2+3j)
print(t)                #([1, 2], 'suig', 1, 1.3, True, (2+3j))
print(type(t))          #<class 'tuple'>
```
### Write a Python program to create a tuple with numbers and print one item.
```
t=(1,2,3,4,5)
print(t,type(t))        #(1, 2, 3, 4, 5) <class 'tuple'>
t=5                     #5 <class 'int'>
print(t,type(t))
t=5,
print(t,type(t))        #(5,) <class 'tuple'>
t=5,3,2,[1,2]           #(5, 3, 2, [1, 2]) <class 'tuple'>
print(t,type(t))
```
### Write a Python program to unpack a tuple in several variables.
```
t=(1,2,3,["a","b","c"])
a,b,c,d=t                    #unpack
print(a,b,c,d)               #1 2 3 ['a', 'b', 'c']
a,b,c,d,e=t                  #ValueError: not enough values to unpack (expected 5, got 4)
```
### Write a Python program to add an item in a tuple.
* tuples are immutable, so we cannot directly add an item to it, instead we add another tuple to create a new tuple.
```
t=(1,2,3,4,5)
t=t+(6,7)
print(t)                            #(1, 2, 3, 4, 5, 6, 7)
#t=t+6,                             #error
t=(1,2,3,4,5)
t=t[:2]+(2.5,2.7)+t[2:]
print(t)                            #(1, 2, 2.5, 2.7, 3, 4, 5)
t=(1,2,3,4,5)
t=list(t)
t.append(6)
t=tuple(t)
print(t)                           #(1, 2, 3, 4, 5, 6)
t=(1,2,3,4,5)
t=list(t)
t.extend([6,7,8,9])                                       #t.extend(range(6,10))       #t.extend((6,7,8,9)) 
t=tuple(t)
print(t)        #(1, 2, 3, 4, 5, 6, 7, 8, 9)
```
### Write a Python program to convert a tuple to a string.
```
t=("s","o","u","n","d")                            
print(t,type(t))                                           #('s', 'o', 'u', 'n', 'd') <class 'tuple'>
s="".join(t)
print(s)                                                   #sound
t=("s","o","u","n","d")
t=str(t)
print(t,type(t))                                           #('s', 'o', 'u', 'n', 'd') <class 'str'>
s="".join(t)
print(s)                                                   #('s', 'o', 'u', 'n', 'd')
```
### Write a Python program to get the 4th element and 4th element from last of a tuple.
```
t=(1,2,3,4,5,6,7,8,9,10)
print(t)                                                   #(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(t[3],t[-4])                                          #4 7
```
### Write a Python program to create the colon of a tuple.
```
import copy
t=(1,2,3,[],"dive",True)
t1=copy.copy(t)
t2=copy.deepcopy(t)
print(t1,id(t1))     #(1, 2, 3, [], 'dive', True) 1895612435808
print(t2,id(t2))     #(1, 2, 3, [], 'dive', True) 1895612592480
t1[3].append(0)
t2[3].append(0)
print(t1,id(t1))    #(1, 2, 3, [0], 'dive', True) 1895612435808
print(t2,id(t2))    #(1, 2, 3, [0], 'dive', True) 1895612592480
print(t,id(t))      #(1, 2, 3, [0], 'dive', True) 1895612435808
```
### Write a Python program to find the repeated items of a tuple.
```
t=(1,2,8,8,8,9,0,4,4,7)
n=int(input("enter the number to find its count in tuple"))
print(t.count(n))
```
* I.e returns int 0 or count
### Write a Python program to check whether an element exists within a tuple.
```
t=(1,2,8,8,8,9,0,4,4,7)
n=int(input("enter the value to find if it exists in tuple"))
try:
    if t.index(n)>=0:
        print(n,"exists in tuple")
except:
    print(n,"not found in tuple")
t=(1,2,8,"hi","sh")
print("hi" in t)           #True
print(4 in t)              #False
```
### Write a Python program to convert a list to a tuple.
```
l=[1,2,8,"hi","sh"]
t=tuple(l)
print(l,type(l))                     #[1, 2, 8, 'hi', 'sh'] <class 'list'>
print(t,type(t))                     #(1, 2, 8, 'hi', 'sh') <class 'tuple'>
```
### Write a Python program to remove an item from a tuple.
```
t=(1,2,8,7,6,4)
n=int(input("enter the index to remove value"))
l=list(t)
l.remove(l[n])
t=tuple(l)
print(t)
t=(1,2,8,7,6,4)
t=t[:n]+t[n+1:]
print(l)
```
### Write a Python program to slice a tuple.
```
t=(1,2,8,7,6,4)
s=t[::-1]              #(4, 6, 7, 8, 2, 1)
print(s)               #(8, 6)
s=t[2::2]
print(s)
```
### Write a Python program to find the index of an item of a tuple.
```
t=(1,2,8,7,6,4)
n=int(input("enter the value to be searched"))
print(n,"found in tuple at",t.index(n),"position")       #the index from which you want to searc
print(n,"found in tuple at",t.index(n,2),"position")     #the segment of the tuple to be searched
print(n,"found in tuple at",t.index(n,2,4),"position")
print(n,"found in tuple at",t.index(0),"position")       #ValueError: tuple.index(x): x not in tuple
### Write a Python program to find the length of a tuple.
t=tuple("abcdef")
print(t,len(t))                        #('a', 'b', 'c', 'd', 'e', 'f') 6
```
### Write a Python program to convert a tuple to a dictionary.
```
t=((1,"a"),(2,"b"),(3,"c"))
d=dict(t)
print(d,type(d))                        #{1: 'a', 2: 'b', 3: 'c'} <class 'dict'>
d1=dict((b, a) for a, b in t)
print(d1,type(d1))                      #{'a': 1, 'b': 2, 'c': 3} <class 'dict'>
```
### Write a Python program to unzip a list of tuples into individual lists.
```
t=((1,"a"),(2,"b"),(3,"c"))
a=list(zip(*t))                #* operator unzips the tuples into independent lists.
print(a)                       #[(1, 2, 3), ('a', 'b', 'c')]
t=((1,"a"),(2,"b"),(3,"c"))
t1=[[a for a,b in t],[b for a,b in t]]          #list comprehension
print(t1)                                       #[[1, 2, 3], ['a', 'b', 'c']]
```
### Write a Python program to reverse a tuple.
```
t=(1,2,3,4,True,"hi",[2,3])
t=t[::-1]
print(t)                         #([2, 3], 'hi', True, 4, 3, 2, 1)
a=("abcde")
b=reversed(a)     
print(b)                         #<reversed object at 0x0000028D5C0B2430>
print(tuple(b))                  #('e', 'd', 'c', 'b', 'a')
print(tuple(reversed(t)))        #(1, 2, 3, 4, True, 'hi', [2, 3])
```
### Write a Python program to convert a list of tuples into a dictionary.
```
t=[("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)]
d=dict(t)
print(d)                        #{'x': 3, 'y': 2, 'z': 1}
d={}
for i,j in t:
    d.setdefault(i,[]).append(j)
print(d)                        #{'x': [1, 2, 3], 'y': [1, 2], 'z': [1]}
```
### Write a Python program to print a tuple with string formatting.
* Sample tuple : (100, 200, 300)
* Output : This is a tuple (100, 200, 300)
```
t=(1,2,3)
print("This is a tuple",t)
print('This is a tuple {0}'.format(t))
```
### Write a Python program to replace last value of tuples in a list.
* Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
* Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
```
a= [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
a=[[i[:-1]+(100,)] for i in a]
print(a)
```
```
a= [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
a=[[(i[0],i[1])+(100,)]for i in a]
print(a)
```
### Write a Python program to remove an empty tuple(s) from a list of tuples.
* Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
* Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']
```
a=[(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
a=[i for i in a if i]                   # put tuple in list if not empty
print(a)
a=[(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
a=filter(None,a)
print(a)                                       #<filter object at 0x000001F8A2A52430>
a=list(a)
print((a))                                     #[('',), ('a', 'b'), ('a', 'b', 'c'), 'd']
```
```
a=[(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
b=[]
for i in a:
    if len(i)!=0:
        b.append(i)
print(b)
```
### Write a Python program to sort a tuple by its float element.
* Sample data: [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
* Expected Output: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]
```
a=[('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
a=sorted(a,key=lambda b:float(b[1]),reverse=True)
print(a)
```
### Write a Python program to count the elements in a list until an element is a tuple.
```
l=[1,2,(0,4),"hi",None,(),("a","b")]
c=0
for i in l:
    if type(i)==tuple:
        break
    c+=1
print("The total number of elements in a list before tuple are:",c)
```
```
l=[1,2,(0,4),"hi",None,(),("a","b")]
c=0
for i in range(len(l)):
    if type(l[i])==tuple:                                                                                
        c+=len(l[i])
print("The total numple of only tuple elements in a list are:",c)
```
```
l=[1,2,(0,4),"hi",None,(),("a","b")]
c=0
for i in l:
    if isinstance(i,tuple):
        break
    c+=1
print("The total number elements in a list before tuple are:",c)
```


 
 

