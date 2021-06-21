def sqrt(x):
    if(x==1 or x==0):
        return x
    i = 1; result = 1
    while result <= x:
        i+=1
        result=i*i
    return i - 1     

print("Sqaure Root oF", 81," is ", sqrt(81))        