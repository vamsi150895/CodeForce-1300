# Python program for the Peter and book problem from codeForce

print('Enter number of pages in the book')
noOfPages = int(input())
print('Enter the number of pages read on each day of the week')
pagesPerDay = list(map(int, input().split()))
sum1 = 0
while(sum1 < noOfPages):
    for weekDay in pagesPerDay:
        sum1 = sum1 + weekDay
        if sum1 >= noOfPages:
            print(pagesPerDay.index(weekDay) + 1)
            exit()