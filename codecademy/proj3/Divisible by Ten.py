"""
CODE CHALLENGE: LOOPS
Divisible by Ten
divisible_by_ten(nums)
"""

#Write your function here
def divisible_by_ten(nums):
  amount = 0
  for num in nums:
    if num % 10 == 0:
      amount += 1
  return amount

#Uncomment the line below when your function is done
print(divisible_by_ten([20, 25, 30, 35, 40]))
