#  Binary search function
def binary_search (sorted_collection: list[int], item: int):
    
    low   = 0
    upper = len(sorted_collection) - 1

    while low <= upper:
        # Find the mid of the index
        mid = (low + upper) // 2
        if sorted_collection[mid] == target:
            return mid
        else:
            if sorted_collection[mid] > target:
                upper = mid + 1
            else:
                low = mid - 1 
    return None

if __name__ == "__main__":
    # Take user input array
    user_input = input("Enter numbers separated by comma:\n").strip()
    # Sorted the array
    collection = sorted(int(item) for item in user_input.split(","))
    # Take the target input to find
    target = int(input("Enter a single number to be found in the list:\n"))
    # Function call and get the index as result
    result = binary_search(collection, target)

    if result is None:
        print(f"{target} was not found in {collection}.")
    else:
        print(f"{target} was found at position {result} in {collection}.")