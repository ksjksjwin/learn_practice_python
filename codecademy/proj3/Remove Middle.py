"""
CODE CHALLENGE: LISTS
Remove Middle
remove_middle(lst, start, end)
"""

#Write your function here
def remove_middle(lst,start,end):
  answer_list = lst[:start] + lst[end+1:]
  return answer_list

#Uncomment the line below when your function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))
