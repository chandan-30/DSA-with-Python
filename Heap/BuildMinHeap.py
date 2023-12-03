def heapify( arr, n, index ) :

    left_child = 2 * index + 1
    right_child = 2 * index + 2
    minimum = index

    if left_child < n and arr[ left_child ] < arr[ index ] :
        minimum = left_child
    if right_child < n and arr[ right_child ] < arr[ minimum ] :
        minimum = right_child
    
    if minimum != index :
        arr[ index ], arr[ minimum ] = arr[ minimum ], arr[ index ] 
        heapify( arr, n, minimum )
    return
    
    

def buildHeap( arr, n ):
    startIndex = n // 2 - 1
    for i in range( startIndex, -1, -1 ) :
        heapify( arr, n, i )
    return arr

def getKSmallestElement( arr, k ) :
    resultSet = []
    arr = buildHeap( arr, len( arr ) )
    resultSet.append( arr[ 0 ] )
    for i in range( 1, k ) :
        arr = buildHeap( arr[ 1: ], len( arr[ 1: ] ) )
        resultSet.append( arr[ 0 ] )
    print( resultSet )
        

arr = [ 15,10,35,19,7,21, 15,6,22,9 ]
# print( buildHeap( arr, len( arr ) ) )
getKSmallestElement( arr, 6 )
    
