# Python program for the blackjack problem from codeForce


print('Enter the sum that is desired: ')
sum1 = int(input())

if sum1 == 10 or (sum1 > 21 and sum1 <= 25):
    print(int('0'))
elif sum1 > 10 and sum1 < 20:
    print(int('4'))
elif sum1 == 20:
    print(int('15'))
elif sum1 == 21:
    print(int('1'))
else:
    print('Sum should be less than 25')