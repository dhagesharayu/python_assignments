 
# Python: Array Exercises
 
### Write a Python program to create an array of 5 integers and display the array items. Access individual element through indexes.
```
import array
#a=array.array('i',["a","b","c","d"])                  #TypeError: an integer is required (got type str)    
a=array.array('i',[1,2,3,4,5])   
print(a)                                               #array('i', [1, 2, 3, 4,5])
for i in a:
    print(i)                                           #Individual elements printed
print("The thrid element in array is: ",a[2],"and last element is: ",a[4])
                                                       #The thrid element in array is:  3 and last element is:  5
```
### Write a Python program to append a new item to the end of the array.
```
import array
a=array.array('i',[1,2,3,4,5])
a.append(6)
print(a)                                           #array('i', [1, 2, 3, 4, 5, 6])
a.extend([7,8])
print(a)                                           #array('i', [1, 2, 3, 4, 5, 6, 7, 8])
```
### Write a Python program to reverse the order of the items in the array.
```
import array
a=array.array('i',[1,2,3,4,5,6,7,8])
a.reverse()
print(a)
```
### Write a Python program to get the length in bytes of one array item in the internal representation.
```
import array
a=array.array('i',[1,2,3,4,5,6,7,8])
#print(a.itemsize())             #Error
print(a.itemsize)                #4(i.e size of an int(max size) 4 bytes)
```
### Write a Python program to get the current memory address and the length in elements of the buffer used to hold an array?s contents and also find the size of the memory buffer in bytes.
```
import array
a=array.array('i',[1,2,3,4,5,6,7,8])
print("The current memmory address of buffer(a(i)):",a.buffer_info()[0])
                                                  #The current memmory address of buffer(a(i)): 2163486407248
print("The length in elements of buffer:",a.buffer_info()[1])
                                                  #The length in elements of buffer: 8
print("The size of the memory buffer in bytes:",a.buffer_info()[1]*a.itemsize)
                                                  #The size of the memory buffer in bytes: 32
```
### Write a Python program to get the number of occurrences of a specified element in an array.
```
import array
a=array.array('i',[1,2,3,4,5,6,7,8,2,8,7])
n=int(input("enter no to check its count in array"))
print(n,"occurs",a.count(n),"times in array")
```
### Write a Python program to append items from inerrable to the end of the array.
*Attach the array to itself or another array
```
import array
a=array.array('i',[1,2,3,4,5])
b=array.array('c',[6,7,8,9,10]) 
                                #ValueError: bad typecode (must be b, B, u, h, H, i, I, l, L, q, Q, f or d),i.e datatype
b=array.array('b',[6,7,8,9,10])
#a.extend(b)                    #TypeError: can only extend with array of same kind
b=array.array('i',[6,7,8,9,10])
a.extend(b)
print(a)                        #array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
```
### Write a Python program to convert an array to an array of machine values and return the bytes representation.
```
import array
a=array.array('b',[65,66,67,68,69])
print(a.tobytes())
s=a.tobytes()
print(s)                                         #b'abcde
```
### Write a Python program to append items from a specified list.
```
import array
b=[1,2,3,4]
a=array.array('i',[])
a.fromlist(b)
print(a)                               #array('i', [1, 2, 3, 4])
a=list(a)
c=array.array('i',[1,2])
c.fromlist(a)
print(c)                               #array('i', [1, 2, 1, 2, 3, 4])
```
### Write a Python program to insert a new item before the second element in an existing array.
* insert()-inserts an element at a specified index
```
import array
a=array.array('i',[1,2,3,4,5])
a.insert(1,9)
print(a)
```
### Write a Python program to remove a specified item using the index from an array.
```
import array
a=array.array('i',[1,2,3,4,5])
print(a.pop(1))                    #2
print(a)                           #array('i', [1, 3, 4, 5])
print(a.remove(3))                 #None
print(a)                           #array('i', [1, 4, 5])
print(a.pop())                     #5
print(a)                           #array('i', [1, 4])
a.remove()                         #TypeError: remove() takes exactly one argument (0 given)
```
### Write a Python program to remove the first occurrence of a specified element from an array.
```
import array
a=array.array('i',[1,2,3,4,5,5,4,3,2,1])
a.remove(1)
a.remove(4)
print(a)                               #array('i', [2, 3, 5, 5, 4, 3, 2, 1])
```
### Write a Python program to convert an array to an ordinary list with the same items.
```
import array
a=array.array('i',[1,2,3,4,5,5,4,3,2,1])
a=list(a)
print(a,type(a))                              #[1, 2, 3, 4, 5, 5, 4, 3, 2, 1] <class 'list'>
import array
a=array.array('i',[1,2,3,4,5,5,4,3,2,1])
a.tolist()
print(a,type(a))                              #array('i', [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]) <class 'array.array'>
a=a.tolist()
print(a,type(a))                              #[1, 2, 3, 4, 5, 5, 4, 3, 2, 1] <class 'list'>
```
### Write a Python program to find whether a given array of integers contains any duplicate element. Return true if any value appears at least twice in the said array and return false if every element is distinct.
```
def duplicate(z):
    if len(z)==len(set(z)):
        print("The array does not contain duplicate")
    else:
        print("The array contains duplicate")

import array
a=array.array('i',[1,2,3,4,5])
b=array.array('i',[5,4,3,2,1])
b.extend(a)
duplicate(a)
duplicate(b)
 ```   
### Write a Python program to find the first duplicate element in a given array of integers. Return -1 If there are no such elements.
```
def first_dupl(z):
    if len(z)==len(set(z)):
        return -1
    else:
        for i in range(len(z)-1):
            for j in range(i+1,len(z)):
                if z[i]==z[j]:
                    return z[i]
import array
a=array.array('i',[1,2,3,4,5])
b=array.array('i',[5,4,3,2,1])
b.extend(a)
print(a,b)                                       #array('i', [1, 2, 3, 4, 5]) array('i', [5, 4, 3, 2, 1, 1, 2, 3, 4, 5])
print(first_dupl(a))                             #-1
print(first_dupl(b))                             #5
```    



