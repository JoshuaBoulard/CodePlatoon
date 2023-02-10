def char_count(str):
  charDict = {}
  for letter in str: 
    if letter in charDict:
      charDict[letter] += 1
    else: charDict[letter] = 1
  print(charDict)

char_count('apple')