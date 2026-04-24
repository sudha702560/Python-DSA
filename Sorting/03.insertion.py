def insertion_sort(arr):
    """
    Sorts a list in-place using Insertion Sort algorithm.

    How it works:
    - Builds the final sorted array one element at a time.
    - Takes one element from the unsorted part and inserts it into its
      correct position within the sorted part.
    - Shifts larger elements one position to the right to make space.

    Time Complexity:
        Best Case:    O(n)   (already sorted array)
        Average Case: O(n^2)
        Worst Case:   O(n^2) (reverse sorted array)

    Space Complexity: O(1) (in‑place)

    Properties:
        - Stable: equal elements keep their original relative order.
        - Efficient for small or nearly sorted datasets.
    """
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1

        # Move elements of arr[0..i-1] that are greater than key
        # one position ahead to make space for the key
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        # Place key at its correct position
        arr[j + 1] = key

def print_array(arr):
    """Prints list elements separated by a space."""
    print(' '.join(map(str, arr)))

if __name__ == "__main__":
    arr = [19, 6, 10, 4, 43]
    print("Sorted array in ascending order:")
    insertion_sort(arr)
    print_array(arr)