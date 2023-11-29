def fibDP( n, arr ) :
    if n == 0 :
        return 0
    if n == 1 :
        return 1
    if arr[ n - 1 ] != 0 :
        return arr[ n - 1 ]

    arr[ n - 1 ] = fibDP( n - 2, arr ) + fibDP( n - 1, arr )
    return arr[ n - 1 ]

def dp( n ) :
    arr = [ 0 ] * n
    return fibDP( n, arr )

n = 1000
print( dp( n ) )