"""
Review 

Use a key to get a value from a dictionary
-dict["example"]

Check for existence of keys
.get(key,0)

Find the length of a dictionary
len(dict)

Remove a key: value pair from a dictionary
.pop(value,0)

Iterate through keys and values in dictionaries
.items() --> tuple
for key, value in dict.items():
---> do something
"""

tarot = { 1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}

spread = {}

spread['past'] = tarot.pop(13)

spread['present'] = tarot.pop(22)

spread['future'] = tarot.pop(10)

for key, value in spread.items():
  print("Your {} is the {} card.".format(key,value))
