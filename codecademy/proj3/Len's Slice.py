"""
PYTHON LISTS
Len's Slice
You work at Len's Slice, a new pizza joint in the neighborhood. You are going to use your knowledge of Python lists to organize some of your sales data.
"""

toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

prices = [2,6,1,3,2,7,2]

num_pizzas = len(toppings)

print("We sell " + str(num_pizzas) +" different kinds of pizza!")

pizzas = list(zip(prices,toppings))

pizzas.sort()

print(pizzas)

cheapest_pizza = pizzas[0]

priciest_pizza = pizzas[-1]

three_cheapest = pizzas[:3]

print(three_cheapest)

num_two_dollar_slices = prices.count(2)
