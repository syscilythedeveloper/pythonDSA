
def twoSum(nums, target):
        #create hashmap 
        #use enumerate to get value and index 
        ##while iterating through the list
        #get the difference between the target and the 
        ##curent number 
        #if it's in the hashmap, return that index and the 
        # Input: nums = [4,5,6], target = 10
        # Output: [0,2]

    valueMap = {}

    for i, value in enumerate(nums):
        difference = target - value
        if difference in valueMap:
            return [valueMap[difference], i]
        else: 
            valueMap[value] = i



print(twoSum([4,5,6], 10))