# Ternery search function to find the index of the target element 'x' in a sorted array
def TernerySearch( arr, left, right, x ):
    # Continue the search while the left index is less than or equal to the right index
    while left <= right:
        # Calculate the middle index 1&2 of the current search range
        mid1 = left + ( right - left ) // 3
        mid2 = right - ( right -left ) // 3
        # Check if the middle element is equal to the target value 'x'
        if arr[ mid1 ] == x:
            # If found, return the index of the element
            return mid1
        elif arr[ mid2 ] == x:
            # If found, return the index of the element
            return mid2
        # If the middle element is less than the target value 'x', update the left index
        elif arr [ mid1 ] < x:
            #left = mid1 + 1
            return TernerySearch( arr, mid1 + 1, right, x )
        elif arr [ mid2 ] > x:
            # right = mid2 - 1
            return TernerySearch( arr, left, mid2 - 1, x )
        # If the middle element is greater than the target value 'x', update the right index
        else:
            # right = mid2 - 1
            # left = mid1 + 1
            return TernerySearch( arr, mid1 + 1, mid2 - 1, x )
    
    # If the element is not found, return -1
    return -1

# Example array
arr = [ 10, 20, 30, 40, 50 ]
# Initialize left and right indices for the Ternery search
left = 0
right = len( arr ) - 1

# Perform Ternery search for the value 20 in the array
print( "Element found at index :: ", TernerySearch( arr, left, right, 440 ) )

# Perform Ternery search for the value 320 in the array
print( "Element found at index :: ", TernerySearch( arr, left, right, 50 ) )