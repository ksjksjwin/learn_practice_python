"""
Scrabble
In this project, you will process some data from a group of friends playing scrabble. You will use dictionaries to organize players, words, and points.

There are many ways you can extend this project on your own if you finish and want to get more practice!
"""

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {letter:point for letter, point in zip(letters,points)}

#print(letter_to_points)

letter_to_points[" "] = 0

def score_words(word):
  point_total = 0
  for letters in word:
    if letters in letter_to_points:
    	point_total += letter_to_points[letters]
    else:
      point_total += 0
  return point_total
#print(score_words("TENNIS"))
brownie_points = score_words("BROWNIE")

#print(brownie_points)

player_to_words = {"player1":["BLUE","TENNIS","EXIT"], "wordNerd": ["EARTH","EYES", "MACHINE"], "LexiCon":["ERASER","BELLY","HUSKY"], "ProfReader":["ZAP","COMA","PERIOD"]}


player_to_points = {}

for key, value in player_to_words.items():
  player = key
  words = value
  
  player_points = 0
  for word in words:
    player_points += score_words(word)
    
  
  player_to_points[player] = player_points
  
print(player_to_points)
