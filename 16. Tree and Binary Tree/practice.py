def deleteDeepestNode(rootNode, dNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value is dNode:
                root.value = None
                return
            if root.value.right_child:
                if root.value.right_child is dNode:
                    root.value.right_child = None
                    return
                else:
                    customQueue.enqueue(root.value.right_child)
            if root.value.left_child:
                if root.value.left_child is dNode:
                    root.value.left_child = None
                    return
                else:
                    customQueue.enqueue(root.value.left_child)