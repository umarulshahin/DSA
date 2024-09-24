

#* Hash map using linked list for collision handling

class Node:
    
    def __init__(self,key,val):
        
        self.key=key
        self.val=val
        self.ref=None
        
class hash_table:
    
    def __init__(self,capacity):
        
        self.capacity=capacity
        self.size=0
        self.table= [None] * capacity
        
    def _hash(self,key):
        
        return hash(key)%self.capacity
    
    def insert(self,key,val):
        
        ind=self._hash(key)
        
        if self.table[ind] is None:
            self.table[ind]=Node(key,val)
            self.size+=1
            
        else:
            curr=self.table[ind]
            while curr:
                
                if curr.key == key:
                    curr.val=val
                    return 
                curr=curr.ref
            new_node=Node(key,val)
            new_node.ref = self.table[ind]
            self.table[ind] = new_node
            self.size += 1
            
    def search(self,key):
        
        ind=self._hash(key)
        curr=self.table[ind]
        while curr:
            
            if curr.key == key:
                
                return curr.val
            curr=curr.ref
        raise KeyError(key)
    
    def remove(self,key):
        
        ind=self._hash(key)
        pre=None
        curr=self.table[ind]
        while curr:
            
            if curr.key == key:
                if pre:
                    pre.ref=curr.ref
                else:
                    self.table[ind]=curr.ref
                self.size-=1
                return
            pre=curr
            curr=curr.ref
        raise KeyError(key)
    
    
h=hash_table(5)
h.insert("shahin",30)
h.insert("shahin1",330)
h.insert("shahin3",50)
h.insert("shahin2",40)
h.insert("shahin5",60)
h.remove("shahin")

print(h.search("shahin1"))
            
            