"""
Given an array of integer as input, print true if two even numbers appear next to each other in the array.
Input-> [1,2,3,4,5,6]
Output-> 2Evens : false
"""

ls = [2,4,5,7,8,9,10]
for i in ls:
  e = (i%2==0)
if (i==e) and ((i+1)==e):
  print("2Even: True")
else:
  print("2Even: False")
