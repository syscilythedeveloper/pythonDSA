class Node: 
    def __init__(self, value):
        self.value = value 
        self.next = None 


class LinkedList: 
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length =1 

    def print_list(self):
        values = []
        temp = self.head
        while temp is not None:
            values.append(str(temp.value))
            temp = temp.next
        print(" -> ".join(values))

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else: 
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1
        return True 
    
    def pop(self):
        if self.length == 0:
            return None
        
        temp = self.head 
        pre = self.head
        while temp.next: 
            pre = temp 
            temp = temp.next 
        self.tail = pre
        self.tail.next = None
        self.length -=1

        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0: 
            self.head = new_node
            self.tail = new_node
        else: 
            new_node.next = self.head 
            self.head = new_node
        self.length+=1
        return True
    
    def pop_first(self): 
        if self.length == 0: 
            return None
        else: 
            temp = self.head 
            self.head = self.head.next 
            temp.next = None
            self.length -=1
        
        if self.length == 0: 
            self.tail = None
        return temp 
    




    def get(self, index):
        if index < 0 or index >=self.length: 
            return None 
        temp = self.head 
        for _ in range(index):
            temp = temp.next 
        return temp
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp: 
            temp.value = value
            return True
        return False
    
    def insert(self, index, value): 
        if index <0 or index > self.length: 
            return False 
        if index == 0: 
            return self.prepend(value)
        if index == self.length: 
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index-1)
        new_node.next = temp.next 
        temp.next = new_node
        return True
    
    def remove(self, index):
        if index <0 or index >= self.length: 
            return None 
        if index == 0: 
            return self.pop_first()
        if index == self.length-1:
            return self.pop()
        prev = self.get(index - 1)
        temp = prev.next 
        prev.next = temp.next 
        temp.next = None
        self.length-=1
        return True

    def reverse(self):
        if self.length <= 1:
            return

        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

        # This line is crucial - it ensures the last node (now first) points to the correct next node
        self.head.next = before

        print("Debug - Final head:", self.head.value)
        print("Debug - Final tail:", self.tail.value)
    
    def find_middle_node(self):
       slow = self.head 
       fast = self.head

       while fast is not None and fast.next is not None: 
           slow = slow.next
           fast = fast.next.next
       return slow
    def find_kth_from_end(ll, k):
        slow = fast = ll.head 
        
        for _ in range (k): 
            if fast is None: 
                return None 
            fast = fast.next
            
        while fast is not None: 
            slow = slow.next 
            fast = fast.next 
        return slow
    
    def remove_duplicates(self):
        #create empty set 
        values = set()
        previous = None 
        current = self.head
        
        while current is not None: 
            if current.value in values:
                previous.next = current.next 
                self.length-=1
            else: 
                values.add(current.value)
                previous = current
            current = current.next

    

        


        

my_linked_list = LinkedList(0)
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.find_middle_node()