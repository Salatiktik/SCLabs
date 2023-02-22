import constants as cnst

def operation(first:float or int,second:float or int,operator:str):
    print(operator)
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

print("enter first, second numbers and operation add/sub/mult/div\n")
first = int(input(int))
second = int(input(int))
operator = input(str)

print("The result of operation: ", operation(first,second,operator))