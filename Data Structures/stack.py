class Stack :
    def __init__( this ) :
        this.stac = []
        this.len = 0

    def pop( this ) :
        if this.len == 0 :
            print( "There's nothing left to remove " )
            return
        this.len -= 1
        return this.stac.pop()

    
    def push( this, data ) :
        this.stac.append( data )
        this.len += 1

S = Stack()
S.push( 1 )
S.push( 2 )
S.push( 3 )
S.pop()
S.push( 4 )
print( S.stac, "len = ", S.len )