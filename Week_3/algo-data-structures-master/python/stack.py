class Stack:
  # write your __init__ method here that should store a 'total' value which is the total number of elements in the Stack and a 'stack' value which is an array of stored values in the Stack

  def __init__(self):
    self._stack = []
    self.total = 0

  def push(self, data):
    self._stack.append(data)
    return self._stack

  def pop(self):
    self._stack.pop()

  def size(self):
    self.total = len(self._stack)
    return self.total

stack = Stack()
stack.push(5)
stack.push(6)
stack.push(7)
stack.pop()

print(stack.push(8))
print(stack.size())