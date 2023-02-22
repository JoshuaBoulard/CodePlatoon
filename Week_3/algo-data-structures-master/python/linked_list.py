class LinkList:
  # write your __init__ method here that should store a 'head' value which the first Node in the LinkedList and a 'length' value which is the total number of Nodes in the LinkedList
  def __init__(self, head):
    self.length = 0
    self.head = None

  def add(self, data):
    new_node = Node(data)
    if self.head == None:

      self.head = new_node

    else:

      current_node = self.head

      while current_node.next:
        current_node = current_node.next
      current_node.next = new_node

    self.length += 1


  def remove(self, data):
    #In here, you want to essentially take the previous node to the one you're pointing at, and reassign the next value
    #to the one after your current node.  It still exists, but it is no longer a part of the linked list.
    pass
    
  def get(self, element_to_get):
    pass
    

# ----- Node ------
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

train = LinkList()
train.add(3)
train.add(4)
train.add(5)
train.add(6)

cur = train.head

while cur:
  print(cur.data)
  cur = cur.next