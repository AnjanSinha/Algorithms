#Recursive function
def Recursive(num):
    fact = 1
    if num!= 1:
        fact = num * Recursive(num-1)
    return fact

print(Recursive(5))

#Iterative
def Iterative(num):
    fact = 1
    for i in range(num):
        fact *= num
        num -=1
    return fact

print(Iterative(5))