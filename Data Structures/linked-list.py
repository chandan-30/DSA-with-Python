class Node:
    def __init__( this, data ) :
        this.data = data
        this.next = None

class Linkedlist:
    def __init__( this, data ) :
        this.len = 1
        this.head = this.tail = Node( data )

    
    def insertAtBeg( this, data ) :
        new_node = Node( data )
        new_node.next = this.head
        this.head = new_node
        this.len += 1

    def insertAtIndex( this, data, index ) :
        if index == 0 :
            this.insertAtBeg( data )
            return
        if index == this.len :
            this.insertAtEnd( data )
            return

        node = this.goToNode( index - 1 )
        new_node = Node( data )
        new_node.next = node.next
        node.next = new_node
        this.len += 1

    def deleteNode( this, index ) :
        if index == 0 :
            this.head = this.head.next
            this.len -= 1
            return
        node = this.goToNode( index - 1 )
        node.next = node.next.next
        this.len -= 1
        return
    
    def goToNode( this, index ) :
        if index > this.len :
            print( "index out of range " )
            return
        k = 0
        temp = this.head
        while k != index :
            temp = temp.next
            k += 1
        return temp


    
    def insertAtEnd( this, data ) :
        new_node = Node( data )
        this.tail.next = new_node
        this.tail = new_node
        this.len += 1
    
    def printList( this ) :
        temp = this.head
        while temp :
            print( temp.data, "->", end=" " )
            temp = temp.next
    

new_list = Linkedlist( 1 )
new_list.insertAtBeg( 0 )
new_list.insertAtEnd( 2 )
new_list.insertAtIndex( 1.5, 2 )
new_list.insertAtIndex( 3, 4 )
new_list.deleteNode( 0 )
new_list.printList()


    