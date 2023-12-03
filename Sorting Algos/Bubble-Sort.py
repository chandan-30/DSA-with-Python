'''
    Time Complexity will be n * ( n - 1 ) = O(n*2)
'''

def bubbleSort( arr ) :
    for i in range( len( arr ) ) :
        for j in range( i + 1, len( arr ) ) :
            if arr[ j ] < arr[ i ]:
                arr[ i ], arr[ j ] = arr[ j ], arr[ i ]
    return arr


arr = [ 1,66,44, 101 ,2,7,99 ]
print( "Sorted array:: ", bubbleSort( arr ) )