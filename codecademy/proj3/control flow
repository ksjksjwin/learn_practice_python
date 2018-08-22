"""
PYTHON CONTROL FLOW
Sal's Shipping
Sal runs the biggest shipping company in the tri-county area, Sal's Shippers. Sal wants to make sure that every single one of his customers has the best, and most affordable experience shipping their packages. In this project, you'll build a program that will take the weight of a package and determine the cheapest way to ship that package using Sal's Shippers.

Sal's Shippers has several different options for a customer to ship their package. They have ground shipping, which is a small flat charge plus a rate based on the weight of your package. Premium ground shipping, which is a much higher flat charge, but you aren't charged for weight. They recently also implemented drone shipping, which has no flat charge, but the rate based on weight is triple the rate of ground shipping.

Here are the prices:

Ground Shipping

Weight of Package	Price per Pound	Flat Charge
2 pounds or less	$1.50	$20.00
Over 2 pounds but less than or equal to 6 pounds	$3.00	$20.00
Over 6 pounds but less than or equal to 10 pounds	$4.00	$20.00
Over 10 pounds	$4.75	$20.00
Drone Shipping

Weight of Package	Price per Pound	Flat Charge
2 pounds or less	$4.50	$00.00
Over 2 pounds but less than or equal to 6 pounds	$9.00	$00.00
Over 6 pounds but less than or equal to 10 pounds	$12.00	$00.00
Over 10 pounds	$14.25	$00.00
Premium Ground Shipping

Flat charge: $125.00

Write a program that asks the user for the weight of their package and then tells them which method of shipping is cheapest and how much it will cost to ship their package using Sal's Shippers.
"""

def cost_ground(weight):
  if(weight <= 2):
    return 1.50*weight + 20.00
  elif(weight >= 2) and (weight <= 6):
    return 3.00*weight + 20.00
  elif(weight >= 6) and (weight <= 10):
    return 4.00*weight + 20.00
  else:
    return 4.75*weight + 20.00
  
#print(cost_ground(8.4))

premium_ground = 125.00

def cost_drone(weight):
  if(weight <= 2):
    return 4.50*weight
  elif(weight >= 2) and (weight <= 6):
    return 9.00*weight 
  elif(weight >= 6) and (weight <= 10):
    return 12.00*weight 
  else:
    return 14.25*weight
  
#print(cost_drone(1.5))  

def cheap_choice(weight):
  if(cost_ground(weight) < cost_drone(weight)) and (cost_ground(weight) < premium_ground):
    print("cost_ground is cheapest option")
    print("price is " + str(cost_ground(weight)))
    return cost_ground(weight)
  elif(cost_ground(weight) > cost_drone(weight)) and (cost_drone(weight) < premium_ground):
    print("cost_drone is cheapest option")
    print("price is " + str(cost_drone(weight)))
    return cost_drone(weight)
  else:
    print("premium_ground is cheapest option")
    print("price is " + str(premium_ground))
    return premium_ground
  
#print(cheap_choice(4.8))
#print(cheap_choice(41.5))
