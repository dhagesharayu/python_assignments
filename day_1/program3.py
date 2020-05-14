'''
3. Arrange String characters such that lowercase letters should come first
Given input String of combination of the lower and upper case arrange characters in such a way that all
lowercase letters should come first.
Expected Output:
input_String = PyNaTive
arranging characters giving precedence to lowercase letters
aeiNPTvy
arranging characters giving precedence to lowercase letters:
yaivePNT
'''
def arrange(s):
    l=[]
    u=[]
    for i in s:
        if i.islower():
            l.append(i)
        else:
            u.append(i)
    return "".join(l+u)
s=input("Enter the string to be arranged:")
print(arrange(s))
