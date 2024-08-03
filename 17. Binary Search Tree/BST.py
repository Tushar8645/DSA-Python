import queue_linked_list as queue


class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


def insertNode(root_node, node_value):
    if root_node.data == None:
        root_node.data = node_value
    elif node_value <= root_node.data:
        if root_node.left_child is None:
            root_node.left_child = BSTNode(node_value)
        else:
            insertNode(root_node.left_child, node_value)
    else:
        if root_node.right_child is None:
            root_node.right_child = BSTNode(node_value)
        else:
            insertNode(root_node.right_child, node_value)

    return "The node has been successfully inserted"


def preOrderTraversal(root_node):
    if not root_node:
        return

    print(root_node.data)
    preOrderTraversal(root_node.left_child)
    preOrderTraversal(root_node.right_child)


def inOrderTraversal(root_node):
    if not root_node:
        return

    inOrderTraversal(root_node.left_child)
    print(root_node.data)
    inOrderTraversal(root_node.right_child)


def postOrderTraversal(root_node):
    if not root_node:
        return

    postOrderTraversal(root_node.left_child)
    postOrderTraversal(root_node.right_child)
    print(root_node.data)


def levelOrderTraversal(root_node):
    if not root_node:
        return
    else:
        custom_queue = queue.Queue()
        custom_queue.enqueue(root_node)

        while not (custom_queue.isEmpty()):
            root = custom_queue.dequeue()
            print(root.value.data)

            if root.value.left_child is not None:
                custom_queue.enqueue(root.value.left_child)

            if root.value.right_child is not None:
                custom_queue.enqueue(root.value.right_child)


def searchNode(root_node, node_value):
    if root_node.data == node_value:
        print("The value is found")
    elif node_value < root_node.data:
        if root_node.left_child.data == node_value:
            print("The value is found")
        else:
            searchNode(root_node.left_child, node_value)
    else:
        if root_node.right_child.data == node_value:
            print("The valus is found")
        else:
            searchNode(root_node.right_child, node_value)


def minValueNode(bst_node):
    current = bst_node

    while current.left_child is not None:
        current = current.left_child

    return current


def deleteNode(root_node, node_value):
    if root_node is None:
        return root_node

    if node_value < root_node.data:
        root_node.left_child = deleteNode(root_node.left_child, node_value)
    elif node_value > root_node.data:
        root_node.right_child = deleteNode(root_node.right_child, node_value)
    else:
        if root_node.left_child is None:
            temp = root_node.right_child
            root_node = None

            return temp

        if root_node.right_child is None:
            temp = root_node.left_child
            root_node = None

            return temp

        temp = minValueNode(root_node.right_child)
        root_node.data = temp.data
        root_node.right_child = deleteNode(root_node.right_child, temp.data)

    return root_node


def deleteBST(root_node):
    root_node.data = None
    root_node.left_child = None
    root_node.right_child = None

    return "The Binary Search Tree has been successfully deleted"


if __name__ == "__main__":
    custom_bst = BSTNode(None)
    insertNode(custom_bst, 70)
    insertNode(custom_bst, 50)
    insertNode(custom_bst, 90)
    insertNode(custom_bst, 30)
    insertNode(custom_bst, 60)
    insertNode(custom_bst, 80)
    insertNode(custom_bst, 100)
    insertNode(custom_bst, 20)
    insertNode(custom_bst, 40)

    deleteNode(custom_bst, 90)

    # preOrderTraversal(custom_bst)
    # inOrderTraversal(custom_bst)
    # postOrderTraversal(custom_bst)
    levelOrderTraversal(custom_bst)

    searchNode(custom_bst, 20)

    print(deleteBST(custom_bst))
