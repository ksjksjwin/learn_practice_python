"""
CODE CHALLENGE: LOOPS
Larger Sum
larger_sum(lst1, lst2)
"""

#Write your function here
def larger_sum (lst1,lst2):
  sum1 = 0
  sum2 = 0
  
  for item in lst1:
    sum1 += item
  
  for item in lst2:
    sum2 += item
  
  if sum1 >= sum2:
    return lst1
  else:
    return lst2

#Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))
