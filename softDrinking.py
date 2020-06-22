# Python program for the Soft Drinking problem from codeForce


print('Enter these details separated by a space\nNumber of friends\nNumber of bottles')
print('Milliliters in a bottle\nNumber of limes\nSlices of lime')
print('Amount of salt\nQuantity of each Drink\nQantity of salt for each')

n, k , l, c, d, p, nl, np = input().split()

firstCondition = (int(k) * int (l)) / int(n)
secondCondition = int(c) * int (d)
thirdCondition = int(p) / int (np)

print('The number of toasts each friend can make will be:', int((min(firstCondition, secondCondition, thirdCondition) / int(n))))