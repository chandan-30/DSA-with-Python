def findPow( n, p ) :
    op = 1
    if p == 0 :
        return 1
    if p == 1 :
        return n
    if p % 2 == 0 :
        res = findPow( n, p // 2 )
        op = res * res
    else :
        op = findPow( n, p - 1 ) * n
    return op

num = 2
power = 17
print( findPow( num, power ) )