'''
  ---------- Binary Search ----------
  1. First need to find out the lower bound and upper bound of the list [list must be sorted]
  2. Then Find the mid index. equation -> (lower + upper) // 2 [integer division]
  3. Check with the mid value to the target value
  4. If not match then check of the value is smaller or bigger then the mid value
  5. If it's smaller then change the upper bound and mid will be the new upper bound
  6. If it's bigger then change the lower bound and mid will be the new lower bound
  7. Then again go to step 2 and continue the process
  ------------------------------------
  1. It will improve the time complexity. n(o2)
'''


# Declaring a global value for index position
pos = -1

# Binary Search Function
# It will take two paremeters, First one is List and Second one is target that need to search. 
def binarySearch(givenList, target):
   # initialize the lower and upper bound
    low   = 0
    upper = len(givenList) - 1

    while low <= upper:
        # Find the mid of the index
        mid = (low + upper) // 2
        if givenList[mid] == target:
            globals()['pos'] = mid
            return True
        else:
            if givenList[mid] > target:
                upper = mid + 1
            else:
                low = mid - 1 
    return False


#Given a list
searchList = [0, 7, 9, 22, 56, 78, 85, 90, 105]

# Need to find the target
target = 78

# check the target in the list by calling the function

if binarySearch(searchList, target):
    print('Found the element at the index of -> ', pos)
else:
    print('Not Found the element in the list')


'''
----------- Drawbacks -----------
1. Must have the sorted array
---------------------------------
'''