'''
  ------- Linear Search ----------
  It is sequencial search. It will check the whole list one by one check the element.
  if find the element then it will stop.
  --------------------------------
'''

# Declaring a global value for index position
pos = -1

#Linear Search Function
# It will take two paremeters, First one is List and Second one is target that need to search. 
def linearSearch(givenList, target):
   # starting index initial
    i = 0
    while i < len(givenList):
        if givenList[i] == target:
            globals()['pos'] = i
            return True
        i = i + 1
    return False


#Given a list
searchList = [5, 22, 85, 4, 0, 7, 9]

# Need to find the target
target = 11

# check the target in the list by calling the function

if linearSearch(searchList, target):
    print('Found the element at the index of -> ', pos)
else:
    print('Not Found the element in the list')


'''
----------- Drawbacks -----------
1. Requires an n/2 check, that's time consuming. n(0)
2. Not so efficient
---------------------------------
'''