'''
    Time Complexity will be n * ( n - 1 ) = O(n*2)
'''

def insertionSort( arr ) :
    
    for i in range( 1, len( arr ) ) :
        j = i - 1
        key = arr[ i ]
        while j >= 0 and key < arr[ j ] :
            arr[ j + 1 ] = arr[ j ]
            j = j - 1
        arr[ j + 1] = key
    return arr


arr = [ 1,66,44, 101 ,2,7,99,86 ]
print( "Sorted array:: ", insertionSort( arr ) )