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

    def add_begin(self,data):
        new_node= Node(data)
        new_node.ref=self.head
        self.head=new_node
        
    def reverse_list(self):
        self.head=self.reverse(self.head,None)
        
    def reverse(self,head,prev):
        
        if not head:
            return prev
        
        next=head.ref
        head.ref=prev
        return self.reverse(next,head)
        

l=Link_list()
l.add_begin(10)
l.add_begin(20)
l.add_begin(30)
l.reverse_list()

l.traverse()