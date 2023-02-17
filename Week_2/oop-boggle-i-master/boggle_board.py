import random
import string

class BoggleBoard:
  
  def __init__(self, name):
    self.name = name
  
  def __str__(self):
    return f"{self.name}:\n____\n____\n____\n____"

  def shake(self):
    board_array = []
    i = 0
    while i < 4:
      randomLetter = ''.join(random.choices(string.ascii_uppercase, k=4))
      board_array.append(randomLetter)
      i += 1
    joined_board_array = '\n'.join(board_array)
    return f'{self.name}:\n{joined_board_array}'

new_board = BoggleBoard('New')
print(BoggleBoard.shake(new_board))