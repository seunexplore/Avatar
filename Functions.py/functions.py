# def test_function():
#     print(4*2+2)

# test_function()

# def fun2(n:int):
#     print(n**2)

# fun2(4)

# def fun3(a,b,c):
#     print(a,b,c) 

# fun3(1,2,3)
# fun3(a=3, b=1, c=3)

# fun3(2, b=3, a=1) 




def mean(arr):
    mean_value =sum(arr)/len(arr)
    return round(mean_value, 2) 

print("Calculate your mean")
print("Enter your number separated by comma")
vals = input(":>").split(",")
# print(vals)
mapped = list(map(int,vals))

print(mean(mapped))
# print(list(mapped))


