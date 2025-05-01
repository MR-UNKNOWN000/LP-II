def selectionSort(arr):
    n = len(arr)

    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

# Main function
if __name__ == '__main__':
    arr = list(map(int, input("Enter the elements separated by space: ").split()))
    print("Original array:", arr)
    sorted_arr = selectionSort(arr)
    print("Sorted array:", sorted_arr)

    '''✅ Title:
Sorting using Selection Sort Algorithm

✅ Algorithm Steps:
Start from index i = 0 to n-1.

Assume the i-th element is the minimum.

Traverse the rest of the array to find the actual minimum.

Swap the found minimum element with the element at index i.

Repeat for the next index.

✅ Python Output Example:
yaml
Copy
Edit
Enter the elements separated by space: 64 25 12 22 11  
Original array: [64, 25, 12, 22, 11]  
Sorted array: [11, 12, 22, 25, 64]
✅ Time and Space Complexity:
Time Complexity:

Worst Case: O(n²)

Best Case: O(n²)

Average Case: O(n²)

Space Complexity: O(1) (In-place sorting)

✅ Short Theory:
Selection Sort is a simple comparison-based sorting algorithm. It repeatedly selects the smallest (or largest) element from the unsorted part of the list and places it at the beginning. It is not stable and performs poorly on large lists.

✅ Features:
In-place algorithm (no extra memory used).

Performs well on small datasets.

Easy to implement and understand.

Not suitable for large data due to O(n²) time.

✅ Viva Questions & Answers:
Q1: What is the basic idea of selection sort?
A1: Repeatedly find the minimum element and place it at the correct position.

Q2: Is selection sort stable?
A2: No, because it swaps non-adjacent elements.

Q3: What is the time complexity of selection sort?
A3: O(n²) for all cases.

Q4: What is the space complexity?
A4: O(1), because it sorts the array in place.

Q5: What is the number of comparisons in selection sort?
A5: For n elements, it performs (n * (n - 1)) / 2 comparisons.

Q6: Can we use selection sort on linked lists?
A6: It's not efficient for linked lists because random access is not supported.

Q7: Is selection sort better than bubble sort?
A7: It performs fewer swaps but still has the same time complexity.

Q8: Can selection sort be used for descending order?
A8: Yes, by selecting the maximum instead of the minimum in each pass.'''