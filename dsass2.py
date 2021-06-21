def sameValueAndIndex(arr, n):
    for i in range(n):
        
        if arr[0] is i:
           return i
    return -1
arr = [10,2,4,6,74,2]
n = len(arr)
print(str(sameValueAndIndex(arr, n)))
