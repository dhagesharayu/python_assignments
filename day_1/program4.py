'''
4. Given a string, return the sum and average of the digits that appear in the string, ignoring all other
characters
For Example: –
sumAndAverage("English = 78 Science = 83 Math = 68 History = 65") = sum 294 Percentage is 73.5
Solution:
 import r
 '''
import re
def sumavg(s):
    a=[int(i) for i in re.findall("\d{2}",s)]
  
    print("the sum of scores is:",sum(a),"and the average is",sum(a)/len(a))
    
    
sumAndAverage="English = 78 Science = 83 Math = 68 History = 65"
b=(sumavg(sumAndAverage))
