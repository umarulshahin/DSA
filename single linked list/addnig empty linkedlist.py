# ..................... new node at the biggning ............

class Node:
    
    def __init__(self,data):
        self.data=data
        self.ref=None
        
class Link_list:
    
    def __init__(self):
        
        self.head=None
    
    def traverse(self):
        
        if not self.head :
           print("linked List is Empty")
        else:
            n=self.head
            while n:
                print(n.data,"--->",end=" ")
                n=n.ref
    
    def add_empty(self,data):
        
        if self.head is None:
            new_node=Node(data)
            self.head=new_node
        else:
            print("Linked list is not Empty...")

l=Link_list()
l.add_empty(10)

l.traverse()