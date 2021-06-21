test_list = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11]
]
print("All Element" + str(test_list))
# res = any(13 in sub for sub in test_list)
for i in test_list:
    for k in i:  
        print(k)

res = any(13 in sub for sub in test_list)
  
# printing result
print("Is 13 present in Matrix ? : " + str(res))