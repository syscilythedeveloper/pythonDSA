# Given an integer array nums and an integer k, return the k most frequent elements within the array.

# The test cases are generated such that the answer is always unique.

# You may return the output in any order.

# Input: nums = [1,2,2,3,3,3], k = 2

# Output: [2,3]

from collections import Counter
from itertools import islice

#O(n) solution - bucket sort (map value to index)
# count the occurance of each value, then pop k items 
# make count proporortional to size of input array 
# 
def topKFrequency(nums, k):
    count = {}
    freq = [[] for i in range(len(nums) +1)]
    for n in nums: 
        count[n] = 1 + count.get(n, 0) 
    for n, c in count.items():
        freq[c].append(n)

    res=[]
    for i in range(len(freq) -1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k: 
                return res



#O(n log n)
def topFrequency(nums, k): 
    #make dict of numbers
    ans  = Counter(nums)

    #sort dictionary based on value 
    sorted_ans = dict(sorted(ans.items(), key=lambda item: item[1], reverse=True))

    #make list of out of range up to K 
    top_k_items = list(islice(sorted_ans.items(), k))
   
    output = [item[0] for item in top_k_items]
    return output






print(topKFrequency([1,2,2,3,3,3], k =2))
print(topFrequency([1,2,2,3,3,3], k =2))
print(topFrequency([1,1,1,2,3,3,3,3,3,4,5,5,6,7,8,8,8,8,8,8], k =4))
print(topKFrequency([1,1,1,2,3,3,3,3,3,4,5,5,6,7,8,8,8,8,8,8], k =4))