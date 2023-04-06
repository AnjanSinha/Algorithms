#Idnetify the base case
#Identify the recursive case
#Get closer and closer to the base case and return when needed.

count = 0
def recursion():
    global count #Declaring the count in the loop as a global variable
    print(count)
    if count>3:
        return "Done"
    count +=1
    return recursion()

print(recursion())