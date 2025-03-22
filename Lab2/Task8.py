import time

# Create big_list outside of any function
big_list = list(range(100000, 300001))  # From 100,000 to 300,000 inclusive

def search(lst, target):
    """Simple linear search function"""
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1

def time_search(lst, target, description):
    """Time how long it takes to search for a target in the list"""
    start_time = time.time()
    result = search(lst, target)
    end_time = time.time()
    elapsed_time = (end_time - start_time) * 1000  # Convert to milliseconds
    print(f"Searching for {description} ({target}): {elapsed_time:.4f} ms")
    return elapsed_time

# a. Time searches for specific elements
print("First set of searches:")
time_front = time_search(big_list, 100000, "element at front")
time_middle = time_search(big_list, 200000, "element in middle")
time_back = time_search(big_list, 300000, "element at back")
time_not_found = time_search(big_list, 3, "element not in list")

# b. Repeat the searches to compare times
print("\nSecond set of searches:")
time_front_2 = time_search(big_list, 100000, "element at front")
time_middle_2 = time_search(big_list, 200000, "element in middle")
time_back_2 = time_search(big_list, 300000, "element at back")
time_not_found_2 = time_search(big_list, 3, "element not in list")

# Verify big_list length (optional)
print(f"\nLength of big_list: {len(big_list)}")