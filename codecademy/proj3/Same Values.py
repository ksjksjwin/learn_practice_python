"""
CODE CHALLENGE: LOOPS
Same Values
same_values(lst1, lst2)
"""

#Write your function here
def same_values(lst1,lst2):
  i = 0
  new_lst = []
  while i < len(lst1):
    if lst1[i] == lst2[i]:
      new_lst.append(i)
    i+=1
  return new_lst
#Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))
