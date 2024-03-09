def linear(arr,tar):
    
    for i in range(len(arr)):
        if tar == arr[i]:
            print("tar is found at index:",i)
            break
    else:
        print("tar not found in this list")
    
    
    
arr=[4,1,3,6,7,8]
tar=6
linear(arr,tar)    
    