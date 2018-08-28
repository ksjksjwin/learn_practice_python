"""
CODE CHALLENGE: LOOPS
Max Num
max_num(nums)
"""

#Write your function here
def max_num(nums):
  temp = nums[0]
  for item in nums:
    if item > temp:
      temp = item
  return temp

#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))
