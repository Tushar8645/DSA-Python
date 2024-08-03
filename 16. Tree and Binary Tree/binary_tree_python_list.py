class BinaryTree:
    def __init__(self, size):
        self.custom_list = size * [None]
        self.last_used_index = 0
        self.max_size = size

    def insertNode(self, value):
        if self.last_used_index + 1 == self.max_size:
            return "The Binary Tree is full"

        self.custom_list[self.last_used_index + 1] = value
        self.last_used_index += 1

        return "The value has been successfully inserted"

    def searchNode(self, node_value):
        for i in range(len(self.custom_list)):
            if self.custom_list[i] == node_value:
                return "Success"

        return "Not Found"

    def preOrderTraversal(self, index):
        if index > self.last_used_index:
            return

        print(self.custom_list[index])
        self.preOrderTraversal(index * 2)
        self.preOrderTraversal(index * 2 + 1)

    def inOrderTraversal(self, index):
        if index > self.last_used_index:
            return

        self.inOrderTraversal(index * 2)
        print(self.custom_list[index])
        self.inOrderTraversal(index * 2 + 1)

    def postOrderTraversal(self, index):
        if index > self.last_used_index:
            return

        self.postOrderTraversal(index * 2)
        self.postOrderTraversal(index * 2 + 1)
        print(self.custom_list[index])

    def levelOrderTraversal(self, index):
        for i in range(index, self.last_used_index + 1):
            print(self.custom_list[i])

    def deleteNode(self, value):
        if self.last_used_index == 0:
            return "There is not any node to delete"

        for i in range(1, self.last_used_index + 1):
            if self.custom_list[i] == value:
                self.custom_list[i] = self.custom_list[self.last_used_index]
                self.custom_list[self.last_used_index] = None
                self.last_used_index -= 1

                return "The node has been successfully deleted"

    def deleteBT(self):
        self.custom_list = None
        return "The Binary Tree has been successfully delete"


new_bt = BinaryTree(8)
new_bt.insertNode("Drinks")
new_bt.insertNode("Hot")
new_bt.insertNode("Cold")
new_bt.insertNode("Tea")
new_bt.insertNode("Coffee")

print(new_bt.searchNode("Cold"))

# print(new_bt.deleteNode("Hot"))

# new_bt.preOrderTraversal(1)
# new_bt.inOrderTraversal(1)
# new_bt.postOrderTraversal(1)
new_bt.levelOrderTraversal(1)
