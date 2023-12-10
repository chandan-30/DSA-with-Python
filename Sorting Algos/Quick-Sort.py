def quickSort( arr, p, q ) :
    if p < q :
        m = partition( arr, p, q )
        quickSort( arr, p, m - 1 )
        quickSort( arr, m + 1, q )
        

def partition( arr, p, q ) :
    pivot = arr[ p ]
    i = p
    for j in range( i + 1, q + 1 ) :
        if arr[ j ] <= pivot :
            i = i + 1
            arr[ i ], arr[ j ] = arr[ j ], arr[ i ]
        j += 1
    arr[ i ], arr[ p ] = arr[ p ], arr[ i ]
    return i


#Driver Code
arr = [ 50, 40, 70, 10, 30, 90, 45, 67, 79 ]
p = 0
q = len( arr ) - 1

quickSort( arr, p, q )
print( arr )