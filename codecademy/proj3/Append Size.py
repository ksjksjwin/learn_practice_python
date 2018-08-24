"""
CODE CHALLENGE: LISTS
Append Size
append_size(lst)
"""

#Write your function here
def append_size(lst):
  list_origin_size = len(lst)
  list_combine = lst + list(range(1,list_origin_size+1))
  
  return list_combine

#Uncomment the line below when your function is done
print(append_size([23, 42, 108]))
