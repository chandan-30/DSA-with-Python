''' 
    This is a FAANG Interview question
'''
def maxProfit( arr ) :
    minPrice = 1000000
    maxProfit = 0
    l = len( arr )
    for i in range( l ) :
        if arr[ i ] < minPrice :
            minPrice = arr[ i ]
        elif arr[ i ] - minPrice > maxProfit :
            maxProfit = arr[ i ] - minPrice
        else:
            pass
    return maxProfit


arr = [ 7,5,14,3,6,15,20 ]
print( 'Max profit is:: ', maxProfit( arr ) )