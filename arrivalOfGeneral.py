# Python program for the Arrival of general problem from codeForce


print('How many soldiers in the group? ')
sol = int(input())

print('Enter the heights for the', sol,  ' soldiers: ')

heights = []
heights = input().split()

#Check if we have the correct number of soldiers
if len(heights) != sol:
    print('Re- Enter the heights and number of soldiers')
else:    
    for i in range(0, len(heights)): 
        heights[i] = int(heights[i]) 
    print("The heights are: ", heights)
    
    
maxi = 0
mini = 0
mini_index = 0
maxi_index = 0
for i in range(0,len(heights)):
    if heights[i] > maxi:
        maxi = heights[i]
        maxi_index = heights.index(heights[i])
    if heights[i] <= mini:
        mini = heights[i]
        mini_index = heights.index(heights[i])
        
print('The tallest height of', maxi, 'is at', maxi_index, 'position and the smallest height of', mini, 'is at', mini_index)


if( maxi_index > mini_index):
    
    print('Number of seconds required are: ', (maxi_index-1)+(sol-mini_index)-1)

else:
    print('Number of seconds required are: ', (maxi_index-1)+(sol-mini_index))
	
