def divideAndConquer( arr, i, j ) :
    
    if i == j :
        return [ arr[ i ] ]
    mid = i + ( j - i ) // 2
    sub_arr1 = divideAndConquer( arr, i, mid )
    sub_arr2 = divideAndConquer( arr, mid + 1, j )

    l1 = mid - i + 1
    l2 = j - ( mid + 1 ) + 1
    res = merge( sub_arr1, sub_arr2, l1, l2 )
    return res

def merge( a1, a2, l1, l2 ) :

    res = []
    i = j = 0
    while i < l1 and j < l2 :

        if a1[ i ] < a2[ j ] :
            res.append( a1[ i ] )
            i += 1
        else :
            res.append( a2[ j ] )
            j += 1
        
    res = res + a1[ i: ] + a2[ j: ]
    return res


# Driver Code
arr = [ 50, 70, 65, 13, 80, 62, 98, 27 ]
N = len( arr )
print( divideAndConquer( arr, 0, N - 1 ) )