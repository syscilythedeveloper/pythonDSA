class Node: 
    def __init__(self,value):
        self.value = value 
        self.left = None 
        self.right = None 

class BinarySearchTree: 
    def __init__(self):
        self.root = None 
    
    def BFS(self):
        current_node = self.root
        queue = []
        results = []
        queue.append(current_node)
        while len(queue) > 0: 
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None: 
                queue.append(current_node.left)
            if current_node.right is not None: 
                queue.append(current_node.right)
        return results 
    
    def dfs_pre_order(self):
        results = []
        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left is not None: 
                traverse(current_node.left)
            if current_node.right is not None: 
                traverse(current_node.right)
        traverse(self.root)
        return results
    
    def dfs_post_order(self):
        results = []
        def traverse(current_node): 
               
            if current_node.left is not None: 
                traverse(current_node.left)
            if current_node.right is not None: 
                traverse(current_node.right)
            results.append(current_node.value)
        traverse(self.root)
        return results
    
    def dfs_in_order(self): 
        results = []
        def traverse(current_node): 
               
            if current_node.left is not None: 
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right is not None: 
                traverse(current_node.right)
        traverse(self.root)
        return results






     
          

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
    
    def __r_contains(self, current_node, value):
        if current_node == None: 
            return False 
        if value == current_node.value: 
            return True 
        if value < current_node.value: 
            return self.__r_contains(current_node.left, value) 
        if value > current_node.value: 
            return self.__r_contains(current_node.right, value) 
    
    def r_contains(self, value):
        return self.__r_contains(self.root, value)
    
    def __r_insert(self, current_node, value):
        if current_node == None: 
            return Node(value)
        if value < current_node.value: 
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value: 
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node

    def r_insert(self, value):
        if self.root == None: 
            self.root = Node(value)
        self.__r_insert(self.root, value)

    def min_value(self, current_node):
        while (current_node.left is not None): 
            current_node = current_node.left 
        return current_node.value

    def __delete_node(self, current_node, value):
        if current_node == None: 
            return None 
        if value < current_node.value: 
            current_node.left = self.__delete_node(current_node.left, value)
        elif value > current_node.value: 
            current_node.right = self.__delete_node(current_node.right, value)
        else: 
            if current_node.left == None and current_node.right ==None: 
                return None
            elif current_node.left == None: 
                current_node = current_node.right
            elif current_node.right == None: 
                current_node = current_node.left
            else: 
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right = self.__delete_node(current_node.right, sub_tree_min)
        return current_node       

    def delete_node(self, value):
        self.__delete_node(self.root, value)
        


my_tree = BinarySearchTree()
my_tree.r_insert(2)
my_tree.r_insert(1)
my_tree.r_insert(3)
print("Root: ", my_tree.root.value)
print("Root -> Left: ", my_tree.root.left.value)
print("Root -> Right: ", my_tree.root.right.value)
my_tree.delete_node(2)
print("********Post delete *******")
print("Root: ", my_tree.root.value)
print("Root -> Left: ", my_tree.root.left.value)
print("Root -> Right: ", my_tree.root.right)

firstBinary = BinarySearchTree()
firstBinary.insert(47)
firstBinary.insert(21)
firstBinary.insert(76)
firstBinary.insert(82)
firstBinary.insert(27)
firstBinary.insert(18)
firstBinary.insert(52)
firstBinary.insert(76)
print(firstBinary.BFS())
print(firstBinary.dfs_pre_order())
print(firstBinary.dfs_post_order())
print(firstBinary.dfs_in_order())
# print(firstBinary.min_value(firstBinary.root))
# print(firstBinary.min_value(firstBinary.root.right))
# print(firstBinary.root.value)
# print(firstBinary.root.left.value)
# print(firstBinary.root.right.value)
# print(firstBinary.contains(8))
# print(firstBinary.contains(21))
# print(firstBinary.r_contains(8))
# print(firstBinary.r_contains(21))


