# ------------------------------
# LIST - Python List Operations
# ------------------------------

# A list is an indexed, ordered, and mutable data structure.
# Example:
myList = [12, 3, 4, 34.56, "Hello", True]
# Index:       0   1  2     3        4      5
# Negative:   -6  -5 -4    -3       -2    -1

print("Access element by index:", myList[4])  # Output: Hello

# Add to list
myList.append(100)
print("After append:", myList)

# Slicing
print("Slicing [1:5]:", myList[1:5])
print("Slicing [:6]:", myList[:6])
print("Slicing [3:]:", myList[3:])
print("Full list ([:]):", myList[:])

# ------------------------------
# Looping and Aggregation
# ------------------------------

def sum_elements(lst):
    result = 0
    for i in lst:
        result += i
    return result

def product_elements(lst):
    result = 1
    for i in lst:
        result *= i
    return result

def sum_even_elements(lst):
    result = 0
    for i in lst:
        if i % 2 == 0:
            result += i
    return result

def count_even(lst):
    count = 0
    for i in lst:
        if i % 2 == 0:
            count += 1
    return count

def count_greater_than_k(lst, k):
    count = 0
    for i in lst:
        if i > k:
            count += 1
    return count

def elements_greater_than_k(lst, k):
    result = []
    for i in lst:
        if i > k:
            result.append(i)
    return result

def product_greater_than_k(lst, k):
    result = 1
    for i in lst:
        if i > k:
            result *= i
    return result

# ------------------------------
# Duplicates in List
# ------------------------------

# O(n^2) approach using nested loops
def contains_duplicates_naive(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                return True
    return False

# Efficient approach using set
def contains_duplicates_set(lst):
    return len(lst) != len(set(lst))

# Get actual duplicate values
def get_duplicates(lst):
    seen = set()
    duplicates = []
    for i in lst:
        if i in seen:
            duplicates.append(i)
        else:
            seen.add(i)
    return duplicates

# ------------------------------
# Min/Max Operations
# ------------------------------

nums = [1, 34, 56, 32, 31, 48, 90]

# Method 1: Using built-in max()
print("Max:", max(nums))

# Method 2: Using sorted
print("Max using sort:", sorted(nums)[-1])

# Manual Max
def largest_num(lst):
    max_val = float("-inf")
    for i in lst:
        if i > max_val:
            max_val = i
    return max_val

# Manual Min
def smallest_num(lst):
    min_val = float("inf")
    for i in lst:
        if i < min_val:
            min_val = i
    return min_val

# Product of min and max
def prod_large_small(lst):
    min_val = float("inf")
    max_val = float("-inf")
    for i in lst:
        if i > max_val:
            max_val = i
        if i < min_val:
            min_val = i
    return min_val * max_val  # Use abs() if absolute value needed

# Return list of min and max
def min_max(lst):
    min_val = float("inf")
    max_val = float("-inf")
    for i in lst:
        if i > max_val:
            max_val = i
        if i < min_val:
            min_val = i
    return [max_val, min_val]

# ------------------------------

