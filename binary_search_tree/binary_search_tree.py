class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        curr_node = self
        while(True == True):
            if(value > curr_node.value):
                if curr_node.right != None:
                    curr_node = curr_node.right
                else:
                    curr_node.right = BinarySearchTree(value)
                    break
            else:
                if curr_node.left != None:
                    curr_node = curr_node.left
                else:
                    curr_node.left = BinarySearchTree(value)
                    break

    def contains(self, target):
        pass

    def get_max(self):
        pass

    def for_each(self, cb):
        pass
