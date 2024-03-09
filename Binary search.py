def binary_search(arr,tar):
    
    low=0
    high=len(arr)
    flag=False
    while low <= high: 
        mid=(low+high)//2
        if tar == arr[mid]:
            flag=True
            break
        elif tar > arr[mid]:
            low=mid+1
        elif tar < arr[mid]:
            high=mid-1
    if flag:
        print("Target found at index ",mid)
    else:
        print("target Not found at this list")



arr=[1,2,4,5,6,79]
tar=1
binary_search(arr,tar)