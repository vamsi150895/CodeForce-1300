# Python program for the Kids love candies problem from codeForce

#t = int(input('Enter number of test cases: '))
t = int(input())
minChild = []
sol = []
sum1 = 0 
for i in range(t): 
    #print(i+1,' test case:')
    #n,k = map(int, input('Enter number of Candies and minimum for each kid ').split())
    n,k = map(int, input('').split())
    #N = list(map(int, input('Enter number of Candies of each type').split()))
    N = list(map(int, input().split()))
    if(len(N) != n):
        print('Error, Enter ', n ,' elements')
        exit()
    ###########################################    
    i = -1   
    sum1 = 0     
    for element in N:
        i = i+1
        if element < k:
            continue
        elif True:
            sum1 = sum1 + int((element) / k)
        else:
            print(0)       
    sol.append(sum1)
    
    
for ele in sol:            
    print(ele)
    