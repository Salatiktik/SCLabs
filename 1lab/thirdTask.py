def evenList(list:[]):
    even = []
    for i in list:
        if(i%2 == 0):
            even.append(i)
    
    return even


n = int(input("Enter numbers quantity: "))

list = []

print("Enter numbers:")
for i in range(n):
    list.append(int(input(int)))

print("Even numbers list:", evenList(list))