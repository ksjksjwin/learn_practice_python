"""
- A string is a list of characters.
- A character can be selected from a string using its index string_name[index]. These indices start at 0.
- A 'slice' can be selected from a string. These can be between two indices or can be open-ended, selecting all of the string from a point.
- Strings can be concatenated to make larger strings.
- len() can be used to determine the number of characters in a string.
- Strings can be iterated through using for loops.
- Iterating through strings opens up a huge potential for applications, especially when combined with conditional statements.
"""

def username_generator(first_name,last_name):
  username = ''
  if len(first_name) < 3:
    if len(last_name) < 4:
      username = first_name + last_name
    else:
      username = first_name + last_name[:4]
  else:
    if len(last_name) < 4:
      username = first_name[:3] + last_name
    else:
      username = first_name[:3] + last_name[:4]
  return username

def password_generator(username):
  password = ''
  for char in range(-1,len(username)-1):
    password += username[char]
  return passwordd
