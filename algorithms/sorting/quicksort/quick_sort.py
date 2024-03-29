"""
Recursive implementation of quick sort algorithm.
Best Running Time: O(nlog(n))
Worst Running Time: O(n^2)
Space: O(1)
"""

def partition(arr,left,right,pivot):
    """
    All of the numbers to the left of the pivot index that are greater than
    the pivot are swaped with numbers on the right side of the pivot that are
    smaller than the pivot.
    Returns the left index once the left index is no longer smaller than
    the right index.
    """
    while left <= right:
        while arr[left] < pivot:
            left += 1
        while arr[right] > pivot:
            right -=1
        if left <= right:
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp
            left += 1
            right -= 1
    return left

def quick_sort(arr,left,right):
    """Sorts the input array in place recursively."""
    if left >= right:
        return
    pivot = arr[(left + right) // 2]
    ind = partition(arr,left,right,pivot)
    quick_sort(arr, left, ind-1)
    quick_sort(arr, ind, right)

def sort(arr):
    """Sorts and returns the array."""
    quick_sort(arr,0,len(arr)-1)
    return arr
