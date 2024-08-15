


#Problem: Given an array of integers nums, find all the duplicates in the array using a hash table (dictionary).
# Input: nums = [4, 3, 2, 7, 8, 2, 3, 1]
# Output: [2, 3]
# Explanation: The numbers 2 and 3 appear more than once in the input array.
 
# Input: nums = [1, 2, 3, 4, 5]
# Output: []
# Explanation: There are no duplicates in the input array, so the function returns an empty list [].
 
# Input: nums = [3, 3, 3, 3, 3]
# Output: [3]
# Explanation: The number 3 appears more than once in the input array.
def find_duplicates(nums):
    if nums == []:
        return nums
    dup_Array = []
    hash_map = {}

    for n in nums: 
        if n in hash_map:
            dup_Array.append(n)
            
        else: 
            hash_map[n] = True
    return list(set(dup_Array))

    
def find_duplicates2(nums):
    numCount = {}
    for n in nums:
        numCount[n] = 1 + numCount.get(n, 0)
    
    duplicates = []
    for key, value in numCount.items():
        if value > 1: 
            duplicates.append(key)
    return duplicates



#print ( find_duplicates([1, 2, 3, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 3]) )
print ( find_duplicates2([1, 1, 2, 2, 3]) )
print ( find_duplicates([1, 1, 1, 1, 1]) )
print ( find_duplicates2([1, 1, 1, 1, 1]) )
print ( find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]) )
print ( find_duplicates2([1, 2, 3, 3, 3, 4, 4, 5]) )
# print ( find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]) )
# print ( find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([]) )
print ( find_duplicates2([]) )