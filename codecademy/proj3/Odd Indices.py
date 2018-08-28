"""
CODE CHALLENGE: LOOPS
Odd Indices
odd_indices(lst)
"""

#Write your function here
def odd_indices(lst):
  i = 0
  new_lst = []
  
  while i < len(lst):
    if i % 2 == 0:
      i+=1
      continue
    else:
      new_lst.append(lst[i])
      i+=1
  return new_lst

#Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))
