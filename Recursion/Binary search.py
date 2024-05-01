def binary(arr,tar,s,e):
    
    while s<=e:
        
        m=(s+e)//2
        
        if arr[m] == tar:
            return m
        if arr[m]>tar:
            e=(m-1)
            return binary(arr,tar,s,e)
        if arr[m]<tar:
            s=(m+1)
            return binary(arr,tar,s,e)
        
    no="not found"
    return no


arr=[1, 2, 3, 4, 5, 6, 7, 8, 9]
tar=5
s=0
e=len(arr)
res=binary(arr,tar,s,e)
print("result :",res )