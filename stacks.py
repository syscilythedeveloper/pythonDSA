class Node: 
    def __init__(self, value):
        self.value = value 
        self.next = None 


# class Stack: 
#     def __init__(self, value) :
#         new_node =  Node(value)
#         self.top = new_node
#         self.height = 1 

#     def print_stack(self): 
#         temp = self.top 
#         while temp is not None: 
#             print(temp.value)
#             temp = temp.next

#     def push(self, value):
#         new_node = Node(value)
#         if self.height == 0: 
#             self.top = new_node 
#         else: 
#             new_node.next = self.top 
#             self.top = new_node 

#         self.height +=1 

#     def pop(self): 
#         if self.height == 0: 
#             return None
     
#         else: 
#             temp = self.top
#             self.top = self.top.next
#             temp.next = None 
#             self.height -=1
#             return temp 

class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()
       

def reverse_string(string):
    if len(string) == 0: 
        return string
    stack = Stack()
    newString = ""

    for i in string: 
        stack.push(i)

    while not stack.is_empty() != 0:
        letter = stack.pop()
        newString+=letter
    return newString
    
    

print(reverse_string("target"))
print(reverse_string(""))

