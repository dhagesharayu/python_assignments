'''
5. Given a two list. Create a third list by picking an odd-index element from the first list and even index
elements from second.
For Example:
listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]
 Expected Output:
Element at odd-index positions from list one
[6, 12, 18]
Element at even-index positions from list two
[4, 12, 20, 28]
Printing Final third list
[6, 12, 18, 4, 12, 20, 28]
'''
listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]
l1=[]
l2=[]
for i in listOne[1::2]:
    l1.append(i)
for j in listTwo[0::2]:
    l1.append(j)
l3=l1+l2
print(l3)
