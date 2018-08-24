"""
CODE CHALLENGE: LISTS
Middle Item
middle_element(lst)
"""

#Write your function here

def middle_element(lst):
  if len(lst) % 2 != 0:
    return lst[int(len(lst)/2)]
  else:
    middle_val1 = lst[int(len(lst)/2)] 
    middle_val2 = lst[int(len(lst)/2)-1]
    
    #print(middle_val1)
    #print(middle_val2)
    
    return (middle_val1 + middle_val2) / 2
    

#Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5]))
