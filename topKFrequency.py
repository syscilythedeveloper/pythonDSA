# Given an integer array nums and an integer k, return the k most frequent elements within the array.

# The test cases are generated such that the answer is always unique.

# You may return the output in any order.

# Input: nums = [1,2,2,3,3,3], k = 2

# Output: [2,3]

from collections import Counter
from itertools import islice


def topFrequency(nums, k): 
    ans  = Counter(nums)
    sorted_ans = dict(sorted(ans.items(), key=lambda item: item[1], reverse=True))





    #make list of out of range up to K 
   

    top_k_items = list(islice(sorted_ans.items(), k))
   
    output = [item[0] for item in top_k_items]
    print("Output is: ", output)
    return output






topFrequency([1,2,2,3,3,3], k =2)
topFrequency([1,1,1,2,3,3,3,3,3,4,5,5,6,7,8,8,8,8,8,8], k =4)