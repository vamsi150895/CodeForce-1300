# Python program for the beautiful matrix problem from codeForce

# Initialize matrix 
matrix = [] 
print("Enter the numbers rowwise:") 
i = 0
j = 0
minDist = 0
# For user input 
for i in range(1,6):           
    a =[] 
    for j in range(1,6):      
        inp = int(input())
        a.append(inp) 
        if(inp == 1):
            p = 1
            print(i,j)
            minDist = abs(i - 3) + abs(j - 3) 
    matrix.append(a) 
print('The given matrix:') 
# For printing the matrix 
for i in range(5): 
    for j in range(5): 
        print(matrix[i][j], end = " ") 
    print() 

   
if p == 1: print('The minimum number of steps required are ', minDist)