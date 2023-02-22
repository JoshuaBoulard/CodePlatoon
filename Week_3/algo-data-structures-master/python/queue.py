class Queue:
  # write your __init__ method here that should store a 'total' value which is the total number of elements in the Queue and a 'queue' value which is an array of stored values in the Queue
  def __init__(self):
    self.total = 0
    self._queue = []

  def enqueue(self, data):
    self._queue.append(data)
    self.total += 1

  def dequeue(self):
    # write your code to removes the data to the Queue following FIFO and return the Queue
    val = self._queue[0]
    self._queue = self._queue[1:]
    self.total -= 1
    return val

  def size(self):
    return self.total

test_queue = Queue()
test_queue.enqueue(3)
test_queue.enqueue(6)
test_queue.enqueue(9)

print(test_queue._queue)
print(test_queue.total)
print(test_queue.dequeue())
print(test_queue._queue)
print(test_queue.total)

