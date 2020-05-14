'''
1.
a. Given a number count the total number of digits in a number
For example: The number is 75869, so the output should be
'''

n=int(input("Enter the number to count digits"))
n1=n
c=0
while n>0:
    c+=1
    n=n//10
print("the total number of digits in ",n1,"are",c)

'''
b. Reverse the following list using for loop
list1 = [10, 20, 30, 40, 50]
Expected output:
 50
 40
 30
 20
 10
 '''
list1 = [10, 20, 30, 40, 50]
for i in list1[::-1]:
    print(i)
