def FindMaxAndMin( arr, i, j ) :
    
    if i == j :
        return arr[ i ], arr[ i ]
    if i == j - 1 :
        if arr[ i ] < arr[ j ] :
            return arr[ j ], arr[ i ]
        else :
            return arr[ i ], arr[ j ]
    mid = i + ( j - i ) // 2
    mx1, mn1 = FindMaxAndMin( arr, i, mid )
    mx2, mn2 = FindMaxAndMin( arr, mid + 1, j )
    return max( mx1, mx2 ), min( mn1, mn2 )

#Driver code
arr = [ 20, 39, 45, 65, 21, 44, 89, 92 ]
N = len( arr )
print( FindMaxAndMin( arr, 0, N -1 ) )