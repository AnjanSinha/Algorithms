#Iterative Approach
def reverseString(string):
    rever = ''
    for i in range(len(string), 0, -1):
        rever += string[i-1]
    return rever

#print(reverseString("Hello My name is Anjan"))
#Recursive approach
def reverse_recursive(string):
    if string == '':
        return ''
    else:
        return reverse_recursive(string[1:]) + string[0]

print(reverse_recursive("Banana Umbrella"))
