def Recursive(num): #O(2^n) Exponential Time
    if num<2:
        return num
    return Recursive(num-1) + Recursive(num-2)
print(Recursive(5))
#Time complexity of this fibonacci series is exponential time or O(2^n) that is even worse than O(n^2)

def Iterative(num): #O(n) Linear Time
    arr = [0,1]
    for i in range(2,num+1):
        arr.append(arr[i-1]+arr[i-2])
    return arr[num]
print(Iterative(8))