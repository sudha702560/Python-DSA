
def bubble_sort(arr):
    """
    Sorts a list in-place using Bubble Sort algorithm.
    
    Idea:
    - Compare adjacent elements and swap if they are in wrong order.
    - Repeat passes until no swaps are needed.
    
    Time Complexity: O(n^2) worst-case, O(n) best-case (already sorted).
    Space Complexity: O(1) (in-place).
    Stable: Yes.
    """
    n = len(arr)
    for i in range(n - 1):
        swapped = False  # flag to detect any swap
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap using tuple unpacking (Pythonic)
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

                # arr[j]= 230 , arr[j+1]= 30
                # temp = arr[j] = 230
                # arr[j]= arr[j+1] = 30 
                # arr[j+1] = temp = 230
                # x, y = y , x 
                swapped = True
        # If no swaps occurred, the array is already sorted
        if not swapped:
            break

def print_array(arr):
    """Prints the list elements separated by space."""
    print(' '.join(map(str, arr)))

if __name__ == "__main__":
    arr = [1, 5, 9, 2, 0]
    print("Original Array:")
    print_array(arr)

    bubble_sort(arr)

    print("Sorted Array:")
    print_array(arr)
