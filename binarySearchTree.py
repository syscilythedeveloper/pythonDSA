class Node: 
    def __init__(self,value):
        self.value = value 
        self.left = None 
        self.right = None 

class BinaryTree: 
    def __init__(self):
        self.root = None 
     
          

    def insert(self, value ): 
        new_node = Node(value)
        if self.root == None: 
            self.root = new_node
            return True
        temp = self.root 
        while (True):
            if new_node.value == temp.value: 
                return False
            if new_node.value  < temp.value: 
                if temp.left is None: 
                    temp.left = new_node
                    return True 
                temp = temp.left 
            else: 
                if temp.right is None: 
                    temp.right = new_node 
                    return True 
                temp = temp.right

    def contains(self, value):     
        temp = self.root 
        while temp is not None: 
            if value < temp.value: 
                temp = temp.left 
            elif value > temp.value: 
                temp = temp.right

            else: 
                return True 
        return False 
        

firstBinary = BinaryTree()
firstBinary.insert(2)
firstBinary.insert(1)
firstBinary.insert(3)
print(firstBinary.root.value)
print(firstBinary.root.left.value)
print(firstBinary.root.right.value)
print(firstBinary.contains(8))


