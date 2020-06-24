# Python program for the Effective Approach problem from codeForce


# Input part 
vasya_approach = 0
petya_approach = 0
print('Enter the values as per the problem requirement')
numberOfele = int(input())
elements = list(map(int,input().split()))
numberOfQue = int(input())
searchQue = list(map(int,input().split()))


for each_number in searchQue:
    if each_number in elements:
        indexOfNum = elements.index(each_number)
        vasya_approach = vasya_approach + indexOfNum + 1      # Because index starts from 0
        petya_approach = petya_approach + (numberOfele - indexOfNum)




print(vasya_approach, petya_approach)

