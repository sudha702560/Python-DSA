def selection_sort(arr):
    """
    Sorts a list in-place using Selection Sort algorithm.

    Definition:
    Selection sort repeatedly selects the smallest element from the unsorted
    portion and places it at the correct position.

    Working:
    1. Divide array into sorted (left) and unsorted (right) parts.
    2. For each position i, find the minimum element in the unsorted part.
    3. Swap the minimum element with the element at position i.

    Time Complexity:
        Best Case:    O(n^2)
        Average Case: O(n^2)
        Worst Case:   O(n^2)

    Space Complexity: O(1) (in-place)

    Key Points:
    - Simple to implement
    - Not stable by default (equal elements may change order)
    - Good for small datasets
    - Inefficient for large arrays
    """
    n = len(arr)
    for i in range(n - 1):
        min_idx = i

        # Find the index of the minimum element in unsorted portion
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

# 
        # Swap if a new minimum was found
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

def print_array(arr):
    """Prints list elements separated by two spaces (matching C output style)."""
    print('  '.join(map(str, arr)))

if __name__ == "__main__":
    arr = [10, 1, 2, 9, 8, 19]
    print("Sorted array in Ascending Order:")
    selection_sort(arr)
    print_array(arr)