import constants as cnst

def operation(first:float or int,second:float or int,operator:str):
    if(operator==cnst.OPERATIONS[0]):
        return first+second
    elif(operator==cnst.OPERATIONS[1]):
        return first-second
    elif(operator==cnst.OPERATIONS[2]):
        return first*second
    elif(operator==cnst.OPERATIONS[3]):
        return first/second
    else:
        return "error: wrong operation string, try add/sub/mult/div"

def evenList(list:[]):
    even = []
    for i in list:
        if(i%2 == 0):
            even.append(i)
    
    return even


print("Part 1:")
print("Hello world")

print("Part 2:")
print("\nenter first, second numbers and operation add/sub/mult/div:")
first = int(input(int))
second = int(input(int))
operator = input(str)

print("The result of operation: ", operation(first,second,operator))

print("Part 3:")
n = int(input("Enter numbers quantity: "))
list = []

print("Enter numbers:")
for i in range(n):
    list.append(int(input(int)))

print("Even numbers list:", evenList(list))