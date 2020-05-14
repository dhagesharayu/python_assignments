'''
Given 2 strings, s1 and s2, create a new string by appending s2 in the middle of s1
Expected Outcome:
 appendMiddle("Chrisdem", IamNewString) → "ChrIamNewStringisdem"
 '''
def appendMiddle(s1,s2):
    i=int(len(s1)/2)
    s3=s1[:i-1:]+s2+s1[i-1:]
    return s3
s1=input("Enter string one:")
s2=input("Enter string two to append in middle:")
s3=appendMiddle(s1,s2)
print(s3)
