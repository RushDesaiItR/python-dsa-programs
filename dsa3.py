def kthsmallest(arr, k, n):
    arr.sort()
    return arr[k-1]
def kthbiggest(arr, k, n):
    arr.sort()
    return arr[n-1]    
if __name__=='__main__':
    arr=[2,4,5,2,6,9]
    n=len(arr)
    k=2
print("smallest", kthsmallest(arr, k, n))    
print("biggest", kthbiggest(arr, k, n)) 