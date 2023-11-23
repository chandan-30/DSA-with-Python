# Function for linear search in an array
def linearSearch( arr, x ) :
    # Iterate through the array elements
    for i in range( len( arr ) ) :
        # Check if the current element is equal to the target value 'x'
        if arr[ i ] == x :
             # If found, return the index of the element
            return i
    # If the element is not found, return -1
    return -1

# Example array
arr = [ 10, 20, 30, 40, 50 ]

# Perform linear search for the value 20 in the array
print( "Element found at index :: ", linearSearch( arr, 50 ) )

# Perform linear search for the value 320 in the array
print( "Element found at index :: ", linearSearch( arr, 320 ) )

