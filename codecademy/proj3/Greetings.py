"""
CODE CHALLENGE: LOOPS
Greetings
add_greetings(names)
"""

#Write your function here
def add_greetings(names):
  return ["Hello, " + name for name in names]

#Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))
