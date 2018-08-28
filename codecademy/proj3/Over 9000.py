"""
CODE CHALLENGE: LOOPS
Over 9000
over_nine_thousand(lst)
"""

#Write your function here
def over_nine_thousand(lst):
  sum = 0
  if len(lst) == 0:
    return 0
  for item in lst:
    if sum > 9000:
      return sum
    else:
      sum += item
  return sum

#Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))
