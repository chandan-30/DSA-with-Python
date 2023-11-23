'''
    This is facebook interview question on binary search where we need to find the index of first infinite element in an array which 
    contains all the infinte elements at the extreme right of the array
'''

def infBS( arr, left, right ) :
    while left <= right :
        mid = left + ( right - left ) // 2
        if arr[ mid ] != '~' :
            return infBS( arr, mid + 1, right )
        else :
            return infBS( arr, left, mid - 1 )
    return left

def infBSLengthUnknown( arr ) :
    i = 0
    j = 1
    while arr[ j ] != '~' :
        i = j
        j = j * 2
    left = i
    right = j
    return infBS( arr, left, right )



arr = [ -20, 33, 51, -87, 121, 55, '~','~','~','~','~', ]
left = 0
right = len( arr ) - 1
print( 'index of first infite element: ', infBS( arr, left, right ) )
print( 'index of first infite element: ', infBSLengthUnknown( arr ) )
