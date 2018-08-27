"""
CODE CHALLENGE: LOOPS
Delete Starting Even Numbers
delete_starting_evens(lst)
"""

#Write your function here
def delete_starting_evens(lst):
  i = 0
  while i < len(lst):
    if lst[i] % 2 != 0:
      return lst[i:]
    else:
      i += 1
      continue
  return []

#Uncomment the lines below when your function is done
#print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
#print(delete_starting_evens([4, 8, 10]))
