# Python program for the Peter and book problem from codeForce

print('Enter number of pages in the book')
noOfPages = int(input())
print('Enter the number of pages read on each day of the week')
pagesPerWeek = list(map(int, input().split()))
sum1 = 0
for weekDay in pagesPerWeek:
    sum1 = sum1 + weekDay
    if sum1 >= noOfPages:
        print(pagesPerWeek.index(weekDay) + 1)
        exit()