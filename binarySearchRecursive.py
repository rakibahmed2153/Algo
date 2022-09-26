'''
                ------------------------
                    Time complexity
                ------------------------
    T(n) = if number of element is 1 then it will run 1 time
    T(n) = T(n/2) + 1  ;  n > 1
         = O(log n)
                ------------------------

'''


#  Binary search function
def binary_search_recursive(sorted_collection: list[int], target: int, low: int, upper: int):
    
    if( low == upper ):
        if( sorted_collection[low] == target ):
            return low
        else:
            return None
    else:
        mid = (low + upper)//2
        if( sorted_collection[mid] == target ):
            return mid;
        else:
            if sorted_collection[mid] < target:  
                return binary_search_recursive(sorted_collection, target, mid + 1, upper) 
            else:
                return binary_search_recursive(sorted_collection, target, low, mid-1)   
    return None


if __name__ == "__main__":
    # Take user input array
    user_input = input("Enter numbers separated by comma:\n").strip()
    # Sorted the array
    collection = sorted(int(item) for item in user_input.split(","))
    # Take the target input to find
    target = int(input("Enter a single number to be found in the list:\n"))
    # Function call and get the index as result
    result = binary_search_recursive(collection, target, 0, len(collection))

    if result is None:
        print(f"{target} was not found in {collection}.")
    else:
        print(f"{target} was found at position {result} in {collection}.")