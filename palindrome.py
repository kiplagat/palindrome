# write a function that checks if a variable passed is a palindrome or not 
# what a palindrome is/not 
# input
# output
# l = [1, 2, 3]
# s = "test string"
# l[::]
import re
def is_palindrome(string):
  if type(string) != str:
    return False
  string = string.upper()
  string1 = re.sub("\W+","", string)
  string2 = string1[::-1]
  if string1 == string2:
   return True
  else:
    return False
print(is_palindrome("1A Toyota's a Toyota1"))
