# Binary search function to find the index of the target element 'x' in a sorted array
def binarySearch( arr, left, right, x ):
    # Continue the search while the left index is less than or equal to the right index
    while left <= right:
        # Calculate the middle index of the current search range
        mid = left + ( right - left ) // 2
        # Check if the middle element is equal to the target value 'x'
        if arr[ mid ] == x:
            # If found, return the index of the element
            return mid
        # If the middle element is less than the target value 'x', update the left index
        elif arr [ mid ] < x:
            left = mid + 1
        # If the middle element is greater than the target value 'x', update the right index
        else:
            right = mid - 1
    
    # If the element is not found, return -1
    return -1

# Binary search function using recursive approach to find the index of the target element 'x' in a sorted array
def recursiveBinarySearch( arr, left, right, x ) :
    # Continue the search while the left index is less than or equal to the right index
    while left <= right:
        # Calculate the middle index of the current search range
        mid = left + ( right - left ) // 2
        # Check if the middle element is equal to the target value 'x'
        if arr[ mid ] == x:
            # If found, return the index of the element
            return mid
        # If the middle element is less than the target value 'x', update the left index
        elif arr [ mid ] < x:
           return recursiveBinarySearch( arr, mid + 1, right, x )
        # If the middle element is greater than the target value 'x', update the right index
        else:
            return recursiveBinarySearch( arr, left, mid - 1, x )
    
    # If the element is not found, return -1
    return -1

# Example array
arr = [ 10, 20, 30, 40, 50 ]
# Initialize left and right indices for the binary search
left = 0
right = len( arr ) - 1

# Perform Binary search for the value 20 in the array
print( "Element found at index :: ", recursiveBinarySearch( arr, left, right, 40 ) )

# Perform Binary search for the value 320 in the array
print( "Element found at index :: ", binarySearch( arr, left, right, 10 ) )