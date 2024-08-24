class MaxHeap: 
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index +1 
    
    def _right_child(self, index):
        return 2 * index + 2
    
    def _parent(self, index):
        return (index -1)//2
    
    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) -1

        while current > 0 and self.heap[current] > self.heap[self._parent(current)]: 
            self._swap(current, self._parent(current))
            current = self._parent(current)
            
    def remove(self):
        if len(self.heap ) == 0:
            return None
        
        if len(self.heap) == 1: 
            return self.heap.pop()
        
        max_value = self.heap[0]

        self.heap[0] = self.heap.pop()
        self.sink_down(0)

        return max_value
    
    def sink_down(self, index):
        max_index = index 
        while True: 
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if (left_index < len(self.heap)) and self.heap[left_index] > self.heap[max_index]:
                max_index = left_index

            if (right_index < len(self.heap)) and self.heap[right_index] > self.heap[max_index]:
                max_index = right_index

            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else: 
                return 
            
#Write a function named stream_max that takes as its input a list of integers (nums). The function should return a list of the same length, where each element in the output list is the maximum number seen so far in the input list.

#ex input: [1, 3, 2, 5, 4], output[1, 3, 3, 5, 5].
#ex input: [7, 2, 4, 6, 1], output[7, 7, 7, 7, 7].

def stream_max(nums): 
    outputArr = [0] * len(nums) 
    max_heap = MaxHeap()
    for i, num in enumerate(nums):
        max_heap.insert(num)
        outputArr[i] = max_heap.heap[0]
    return outputArr

print(stream_max([1,3,2,5,4]))
print(stream_max([7, 2, 4, 6, 1]))


# myheap = MaxHeap()
# myheap.insert(95)
# myheap.insert(75)
# myheap.insert(80)

# myheap.insert(55)
# myheap.insert(60)
# myheap.insert(50)

# print(myheap.heap)
# myheap.remove()
# print(myheap.heap)
# myheap.remove()
# print(myheap.heap)