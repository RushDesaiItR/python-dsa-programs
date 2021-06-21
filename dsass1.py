def findOccurance(arr, n, x):
    first = -1
    last = -1
    for i in range(0, n) :
        if (arr[i] != x) :
            continue
        if (first == -1) :
            first = i
        last = i
    if (first != -1) :
        print( "First Occurrence = ", first,
			" \nLast Occurrence = ", last)
  
arr = [1,2,3,1,45,6]
n = len(arr)
x = 6
findOccurance(arr, n, x)         
                  