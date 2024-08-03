import queue_linked_list as queue


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


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


def searchBT(root_node, node_value):
    if not root_node:
        return "The Binary Tree does not exist"
    else:
        custom_queue = queue.Queue()
        custom_queue.enqueue(root_node)

        while not (custom_queue.isEmpty()):
            root = custom_queue.dequeue()

            if root.value.data == node_value:
                return "Success"

            if root.value.left_child is not None:
                custom_queue.enqueue(root.value.left_child)

            if root.value.right_child is not None:
                custom_queue.enqueue(root.value.right_child)

        return "Not Found"


def insertNodeBt(root_node, new_node):
    if not root_node:
        root_node = new_node
    else:
        custom_queue = queue.Queue()
        custom_queue.enqueue(root_node)

        while not (custom_queue.isEmpty()):
            root = custom_queue.dequeue()

            if root.value.left_child is not None:
                custom_queue.enqueue(root.value.left_child)
            else:
                root.value.left_child = new_node
                return "Successfully Inserted"

            if root.value.right_child is not None:
                custom_queue.enqueue(root.value.right_child)
            else:
                root.value.right_child = new_node
                return "Successfully Inserted"


def getDeepestNode(root_node):
    if not root_node:
        return
    else:
        custom_queue = queue.Queue()
        custom_queue.enqueue(root_node)

        while not (custom_queue.isEmpty()):
            root = custom_queue.dequeue()

            if root.value.left_child is not None:
                custom_queue.enqueue(root.value.left_child)

            if root.value.right_child is not None:
                custom_queue.enqueue(root.value.right_child)

        deepest_node = root.value
        return deepest_node


def deleteDeepestNode(root_node, delete_node):
    if not root_node:
        return
    else:
        custom_queue = queue.Queue()
        custom_queue.enqueue(root_node)

        while not (custom_queue.isEmpty()):
            root = custom_queue.dequeue()
        
            if root.value is delete_node:
                root.value = None
                return
            
            if root.value.right_child:
                if root.value.right_child is delete_node:
                    root.value.right_child == None
                    return
                else:
                    custom_queue.enqueue(root.value.right_child)


            if root.value.left_child:
                if root.value.left_child is delete_node:
                    root.value.left_child == None
                    return
                else:
                    custom_queue.enqueue(root.value.left_child)


def deleteNodeBT(root_node, node):
    if not root_node:
        return "The Binary Tree does not exist"
    else:
        custom_queue = queue.Queue()
        custom_queue.enqueue(root_node)

        while not (custom_queue.isEmpty()):
            root = custom_queue.dequeue()

            if root.value.data == node:
                delete_node = getDeepestNode(root_node)
                root.value.data = delete_node.data
                deleteDeepestNode(root_node, delete_node)

                return "The node has been successfully deleted"

            if root.value.left_child is not None:
                custom_queue.enqueue(root.value.left_child)

            if root.value.right_child is not None:
                custom_queue.enqueue(root.value.right_child)

        return "Failed to delete"
    
def deleteBT(root_node):
    root_node.data = None
    root_node.left_child = None
    root_node.right_child = None
    
    return "The Binary Tree has been successfully deleted"


if __name__ == "__main__":
    new_bt = TreeNode("Drinks")
    left = TreeNode("Hot")
    tea = TreeNode("Tea")
    coffee = TreeNode("Coffee")
    left.left_child = tea
    left.right_child = coffee
    right = TreeNode("Cold")
    new_bt.left_child = left
    new_bt.right_child = right

    # new_node = TreeNode("Cola")
    # print(insertNodeBt(new_bt, new_node))

    # preOrderTraversal(new_bt)
    # inOrderTraversal(new_bt)
    # postOrderTraversal(new_bt)
    # levelOrderTraversal(new_bt)

    # print(searchBT(new_bt, "Coffee"))
    levelOrderTraversal(new_bt)
    new_node = getDeepestNode(new_bt)
    deleteDeepestNode(new_bt, new_node)
    print()
    levelOrderTraversal(new_bt)

    deleteBT(new_bt)
    levelOrderTraversal(new_bt)