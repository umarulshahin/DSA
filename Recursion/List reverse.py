def list_reverse(li):
    
    if len(li)<=1:
        return li
    
    return list_reverse(li[1:])+[li[0]]


li=[10,20,30,40,50,60]
val=list_reverse(li)
print(li)
print(val)