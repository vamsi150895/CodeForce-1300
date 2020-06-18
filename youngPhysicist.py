# Python program for the young phsicist problem from codeForce
sum1= 0
sum2= 0
sum3 = 0
lines = int(input('How many lines of three integers do you want? '))

for numbers in range(lines):
    print('Enter the ', numbers+1, ' row')
    sum1 = sum1 + int(input())
    sum2 = sum2 + int(input())
    sum3 = sum3 + int(input())
    
if(sum1 == 0 and sum2 == 0 and sum3 == 0):
    print('YES')
else:
    print('NO')