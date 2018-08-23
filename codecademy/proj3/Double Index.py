"""
CODE CHALLENGE: LISTS
Double Index
double_index(lst, index)
"""

#Write your function here

def double_index(lst,index):
	try:
		lst[index] = lst[index] * 2
		return lst
	except IndexError:
		return lst
    

#Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 2))
