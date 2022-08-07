#Write a Python program to carry out a linear search on a list data structure
#Start from the leftmost element of the list and one by one compare x with each element of the list
#If x matches with an element, return True
#If x doesn’t match with any of the elements, return False

def linear_serch(list, x):
    for item in list:
        if x == item:
            return True
    return False

#List with Strings and Intergers
list = [2, 'Berlin', 6, 9, 5, 7,'Luca', 22, 78, 'Tokyo', 'Joke']

#Search element
x = 'Luca'

if linear_serch(list, x):
    print('Found')
else:
    print('Not Found')



