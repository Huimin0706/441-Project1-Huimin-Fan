from Node import Node
from BST import BinarySearchTree

def main():
    print("*** Problem 2 ***")
    n = Node(10)
    print("\nNode Payload:", n)
    n.left = Node(5)
    print("\nAfter:", n)

    bst = BinarySearchTree()
    for value in [15, 25, 35, 45, 55, 65, 75, 85]:
        bst.insert(value)
    print("\nEmpty:", bst.is_empty(), "\nSize:", bst.size())

    print("\nSearch 15:", bst.search(15))
    print("Search 85:", bst.search(85))
    print("Search 20:", bst.search(20))
    print("Search 90:", bst.search(90))

    print("\nInorder:", bst.inorder())
    print("Preorder:", bst.preorder())
    print("Postorder:", bst.postorder())

    bst.delete(45)
    print("\nAfter delete 45:\n\tSearch 45:", bst.search(45), "\n\tInorder:", bst.inorder())
    bst.delete(15)
    print("\nAfter delete 15:\n\tSearch 15:", bst.search(15), "\n\tInorder:", bst.inorder())
    bst.delete(85)
    print("\nAfter delete 85:\n\tSearch 85:", bst.search(85), "\n\tInorder:", bst.inorder())


if __name__ == '__main__':
    main()