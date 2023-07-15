
class Node:
  def __init__(self, val):
    self.val=val 
    self.next=None 
    
class LL:
  def __init__(self):
    self.head=None 
    self.tail=None
    self.next=None
  def AddNode(self, nod):
    if self.head==None:
      nod.next=None
      self.head=nod 
      self.tail=nod  
    else:
      nod.next=self.head
      self.head=nod
      
  def DeleteNode(self, nodValue):
    myLL=self.head 
    if myLL.val==nodValue:
      self.head=myLL.next
    else:
      while(myLL is not None):
          if myLL.val == nodValue:
              break
          prev = myLL
          myLL = myLL.next

      # if key was not present in linked list
      if(myLL == None):
          return

      # Unlink the node from linked list
      prev.next = myLL.next

      myLL = None
      
  def PrintNodes(self):
    ll = self.head
    while ll!=None:
      print(ll.val)
      ll=ll.next
        

if __name__ == '__main__': 
  lList = LL()
  n1 = Node(1)
  n2 = Node(2)
  n3 = Node(3)
  n4 = Node(4)
  lList.AddNode(n1)
  lList.AddNode(n2)
  lList.AddNode(n3)
  lList.AddNode(n4)
  lList.PrintNodes()
  lList.DeleteNode(2)
  lList.PrintNodes()
  