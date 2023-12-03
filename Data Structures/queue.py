class Queue :
    def __init__( this ) :
        this.que = []
        this.len = 0
    
    def pop( this ) :
        if this.len == 0 :
            print( "There's nothing left to remove " )
            return
        this.len -= 1
        del this.que[ 0 ]

    
    def push( this, data ) :
        this.que.append( data )
        this.len += 1

Q = Queue()
Q.push( 1 )
Q.push( 2 )
Q.push( 3 )
Q.pop()
Q.push( 4 )
print( Q.que, "len = ", Q.len )