"""
Given an array of integer as input, print true if two even numbers appear next to each other in the array.
Input-> [1,2,3,4,5,6]
Output-> 2Evens : false
"""

ls = [1,2,3,4,5,6]
ln = len(ls)
even = 0
for i in range(0,ln):
  e = ls[i]
  even = (e%2==0)
  