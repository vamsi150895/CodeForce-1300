# Python program for the Boy or Girl problem from codeForce


print('Enter the name of the person: ')
name = input()
name = list(name)
new_name = []

for element in name:
    if element not in new_name:
        new_name.append(element)

#print(new_name)

if len(new_name) % 2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')
    
    
################################################
#Alternate Solution 

#print('Enter the name of the person: ')
#name = input()
#name = list(name)
#name = set(name)
#if len(name) % 2 == 0:
#    print('CHAT WITH HER!')
#else:
#    print('IGNORE HIM!')
    
##########################################################
