def rearrange(arr, n ) : 
  j = 0
    for i in range(0, n):
        if (arr[i] < 0):
            print(arr[i])
            temp = arr[i]
            print(temp)
            arr[i] = arr[j]
            print(arr[j])
            arr[j]= temp
            j = j + 1
    print(arr)
    print("=====")
# Driver code
arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
n = len(arr)
rearrange(arr, n)