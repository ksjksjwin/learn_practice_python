"""
CODE CHALLENGE: LOOPS
Reversed List
reversed_list(lst1, lst2)
"""

#Write your function here

def reversed_list(lst1,lst2):
  index = 0
  index_reverse = len(lst2)-1
  while index < len(lst1):
    if lst1[index] == lst2[index_reverse]:
      index += 1
      index_reverse -= 1
      continue
    else:
      return False
  return True
#Uncomment the lines below when your function is done

print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))
