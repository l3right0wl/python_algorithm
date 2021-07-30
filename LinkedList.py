class Node():
  def __init__(self, data):
    self.data = data
    self.next = None
    
class LinkedList:
  def __init__(self):
    self.head = None
    self.nodeCount = 0
    
  def append(self, node):
    if self.head == None:
      self.head = node
    else:
      cur = self.head
      while cur.next != None:
        cur = cur.next
      cur.next = node
     
    
