class Node :
    def __init__( this, data ) :
        this.data = data
        this.left = None
        this.right = None

class Tree :
    def __init__( this ) :
        pass

    def inOrder( this, root ) :
        if root :
            this.inOrder( root.left )
            print( root.data, end=" " )
            this.inOrder( root.right )
    
    def preOrder( this, root ) :
        if root :
            print( root.data, end=" " )
            this.inOrder( root.left )
            this.inOrder( root.right )

    def postOrder( this, root ) :
        if root :
            this.inOrder( root.left )
            this.inOrder( root.right )
            print( root.data, end=" " )

    
    

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

tree = Tree()
tree.inOrder( root )
print()
tree.preOrder( root )
print()
tree.postOrder( root )

