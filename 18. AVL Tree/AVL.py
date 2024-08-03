import queue_linked_list as queue

class AVLNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.height = 1


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


if __name__ == "__main__":
    custom_avl = AVLNode(10)
