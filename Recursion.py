#Idnetify the base case
#Identify the recursive case
#Get closer and closer to the base case and return when needed.

count = 0
def recursion():
    global count
    print(count)
    if count>3:
        return "Done"
    count +=1
    return recursion()

print(recursion())