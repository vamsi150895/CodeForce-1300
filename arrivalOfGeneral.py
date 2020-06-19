# Python program for the Arrival of general problem from codeForce


print('How many soldiers in the group? ')
sol = int(input())

print('Enter the heights for the', sol,  ' soldiers: ')

heights = []
heights = input().split()

if len(heights) < sol:
    print('Re- Enter the heights and number of soldiers')
else:    
    for i in range(0, len(heights)): 
        heights[i] = int(heights[i]) 
    print("The heights are: ", heights)
    
