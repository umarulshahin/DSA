
#* Hash map 


class Hash_table:
    
    def __init__(self):
        self.size=10
        self.arr=[None for i in range(self.size)]
        
    def hash_(self,key):
        
        return hash(key)%self.size
    
    def insert(self,key,val):
        
        ind=self.hash_(key)
        self.arr[ind]=val
        
    def search(self,key):
        ind=self.hash_(key)
        
        return self.arr[ind]
    def delete(self,key):
        ind=self.hash_(key)
        self.arr[ind]=None
        

h=Hash_table()
h.insert("hello",10)
h.insert("hello1",50)
h.insert("hello",30)
h.insert("hello3",20)

print(h.search("hello3"))
h.delete("hello")
print(h.search("hello"))