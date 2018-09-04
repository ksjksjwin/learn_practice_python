"""
common_letters that takes two arguments, string_one and string_two and then returns a list with all of the letters they have in common.
"""

def common_letters(string_one,string_two):
  common = []
  for char in string_one:
    if (char in string_two) and (char not in common):
      common.append(char)
  return common
