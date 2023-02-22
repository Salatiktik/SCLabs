import constants as cnst

def operation(first,second,operator:str):    
    if(operator==cnst.OPERATIONS[0]):
        return first+second
    elif(operator==cnst.OPERATIONS[1]):
        return first-second
    elif(operator==cnst.OPERATIONS[2]):
        return first*second
    elif(operator==cnst.OPERATIONS[3]):
        if(first==second==0):
            return "Singularity"
        elif(second==0):
            return "Infinity"
        else:
            return first/second
    else:
        return operation(first,second,input("error: wrong operation string, try add/sub/mult/div: "))

def evenList(list:[]):
    even = []
    for i in list:
        if(i%2 == 0):
            even.append(i)
    
    return even

good = False

print("Part 1:")
print("Hello world")

print("Part 2:")
while not good:
    try:

        print("\nenter first, second numbers and operation add/sub/mult/div:")

        first = int(input(int))
        second = int(input(int))
        operator = input(str)

        good = True
    except:
        print("Something gone wrong, try again please")
        good = False


print("The result of operation: ", operation(first,second,operator))

good = False

print("Part 3:")
while not good:
    try:
        n = int(input("Enter numbers quantity: "))
        good = True
    except:
        print("Something gone wrong, try again please")
        good = False

list = []

good = False

print("Enter numbers:")
for i in range(n):
    while not good:
        try:
            list.append(int(input(int)))
            good = True
        except:
            print("Something gone wrong, try again please")
            good = False

    good = False

print("Even numbers list:", evenList(list))