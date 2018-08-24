"""
CODE CHALLENGE: LISTS
Every Three Nums
every_three_nums(start)
"""

#Write your function here

def every_three_nums(start):
  if start > 100:
    return []
  else:
    return list(range(start,101,3))

#Uncomment the line below when your function is done
print(every_three_nums(91))
