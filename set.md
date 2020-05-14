# Python Data Types: Sets - Exercises
This all can also be done on set of strings 
 
### Write a Python program to create a set.
```
s={0}                                           data so set otherwise dict
print(s)                                              {0}

a=set()
print(a)                                              set()

b=set([0,1,2,3,4])
print(b)                                         {0, 1, 2, 3, 4}

```


### Write a Python program to iteration over sets.
```
a=set([0,1,2,3,4,5])
for i in a:
    print(i)
```

### Write a Python program to add member(s) in a set.
```
a=set([0,1,2,3,4,5])
a.add(6)                     # single item
print(a)                        {0, 1, 2, 3, 4, 5, 6}
a.update([7,8])           # multiple item
print(a)                       {0, 1, 2, 3, 4, 5, 6, 7, 8}
```


### Write a Python program to remove item(s) from set
```
a=set([0,1,2,3,4,5,6,7,8])
a.pop()
print(a)
a.pop()
print(a)
a.pop(4)   #error
print(a)
```
* I.e removes only from start.

### Write a Python program to remove an item from a set if it is present in the set.
```
a=set([0,1,2,3,4,5,6,7,8])
a.discard(4)   
print(a)                                       {0, 1, 2, 3, 5, 6, 7, 8}
a.discard(7)   
print(a)                                       {0, 1, 2, 3, 5, 6, 8}
```

### Write a Python program to create an intersection of sets.
```
a={1,2,3,4,5}
b={4,5,6,7,8}
c=a&b
print(c)                                                     {4,5}
```

### Write a Python program to create a union of sets.
```
a={1,2,3,4,5}
b={4,5,6,7,8}
c=a|b
print(c)                                          {1, 2, 3, 4, 5, 6, 7, 8}
```

### Write a Python program to create set difference. I.e what is not in a
```
a={1,2,3,4,5}
b={4,5,6,7,8}
c=a&b
d=a-c
print(d)                                {1, 2, 3}
```
### Write a Python program to create a symmetric difference.
```
a={1,2,3,4,5}
b={4,5,6,7,8}
c=a^b
print(c)                          {1, 2, 3, 6, 7, 8}
```

### Write a Python program to issubset and issuperset.
* I.e test whether every element in a is in b and every element in b is in a
```
a={1,2,3,4,5}
b={4,5,6,7,8}
c={1,2}
d={4,5}
print(c<=a)         #issubset                     True
print(c<=b)                                       False
print(a>=d)         #issuperset                   True
print(b>=d)                                       True
```


### Write a Python program to create a shallow copy of sets.
* Note : Shallow copy is a bit-wise copy of an object. A new object is created that has an exact copy of the values in the original object.
```
a={1,2,3,4,5}
b=a.copy
print(b)                     <built-in method copy of set object at 0x0000023AD45DBF20>
a.add(6)
print(b)                     <built-in method copy of set object at 0x0000023AD45DBF20>
print(a)                      {1, 2, 3, 4, 5, 6}
b.add(7)                     Error 'builtin_function_or_method' object has no attribute 'add'
```
### Write a Python program to clear a set.
```
a=set([1,2,3,4,5])
print(a)                                                {1, 2, 3, 4, 5}
a.clear()
print(a)                                                  set()
```
### Write a Python program to use of frozensets.

- **Frozensets** can be created using the function frozenset(). This datatype supports methods like copy(), difference(), intersection(), isdisjoint(), issubset(), issuperset(), symmetric_difference() and union(). Being immutable it does not have method that add or remove elements.
* isdisjoint():-Return True if the set has no elements in common with other. 
* difference():-Return a new set with elements in the set that are not in the others.
```
a=frozenset([1,2,3,4,5])
b=frozenset([4,5,6,7,8])
c=set([9,10,11,12,13])
print(a.isdisjoint(b))                   False
print(a.isdisjoint(c))                   True
print(a.difference(b))                   frozenset({1, 2, 3})
print(a.difference(c))                   frozenset({1, 2, 3, 4, 5})
```


### Write a Python program to find maximum and the minimum value in a set.
```
c=set([9,10,11,12,13])
print(max(c))
print(min(c))
print(c.max())   # error has no attribute
```
### Write a Python program to find the length of a set.
```
c=set([9,10,11,12,13])
print(len(c))
print(c.len())   # error has no attribute
```
 
 
 
 
 
 

