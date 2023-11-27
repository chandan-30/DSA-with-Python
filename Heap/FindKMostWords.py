def heapify( arr, n, index ) :
    l = 2 * index + 1
    r = 2 * index + 2
    maximum = index 
    if l < n : 
        if arr[ l ][ 1 ] > arr[ index ][ 1 ] :
            maximum = l
        if arr[ l ][ 1 ] == arr[ index ][ 1 ] and arr[ l ][ 0 ] < arr[ index ][ 0 ] :
            maximum = l
    if r < n :
        if arr[ r ][ 1 ] > arr[ maximum ][ 1 ] :
            maximum = r
        if arr[ r ][ 1 ] == arr[ maximum ][ 1 ] and arr[ r ][ 0 ] < arr[ maximum ][ 0 ] :
            maximum = r

    if maximum != index :
        arr[ index ], arr[ maximum ] = arr[ maximum ], arr[ index ]
        heapify( arr, n, maximum )

def buildHeap( arr, n ):
    
    N = len( arr )
    startIndex = N // 2 - 1
    for i in range( startIndex, -1, -1 ) :
        heapify( arr, N, i )
    return arr

def getFrequency( arr ) :
    
    _map = dict()
    for i in range( len( arr ) ) :
        if arr[ i ] not in _map :
            _map[ arr[i] ] = 1
        else :
            _map[ arr[ i ] ] += 1

    j = 0
    N = len( _map )
    a = [ 0 ] * N
    for i in _map :
        a[ j ] = ( i, _map[ i ] )
        j += 1
    return a

def getKLargestElement( arr, k ) :
    resultSet = []
    arr = buildHeap( arr, len( arr ) )
    resultSet.append( arr[ 0 ][ 0 ] )
    for i in range( 1, k ) :
        print( resultSet )
        arr = buildHeap( arr[ 1: ], len( arr[ 1: ] ) )
        resultSet.append( arr[ 0 ][ 0 ] )
    print( resultSet )

arr = [ 'priya', 'akshay', 'bhatia', 'arpit', 'priya', 'arpit' ]
N = len( arr )
#print( buildHeap( arr, N ))
a = getFrequency( arr )
getKLargestElement( a, 3 )