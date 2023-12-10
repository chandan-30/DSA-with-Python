'''
    Time Complexity will be n * ( n - 1 ) = O(n*2)
'''

def selectionSort( arr ) :
    
    for i in range( len( arr ) ) :
        min_index = i
        for j in range( i + 1, len( arr ) ) :
            if arr[ j ] < arr[ min_index ]:
                min_index = j
        arr[ i ], arr[ min_index ] = arr[ min_index ], arr[ i ] 
    return arr


arr = [ 177,66,44, 101 ,2,7,99 ]
print( "Sorted array:: ", selectionSort( arr ) )