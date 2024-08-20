
# You have been given a string of lowercase letters.

# Write a function called first_non_repeating_char(string) that finds the first non-repeating character in the given string using a hash table (dictionary). If there is no non-repeating character in the string, the function should return None.

def first_non_repeating_char(string):
    chars = { }

    for letter in string: 
        chars[letter] = 1 + chars.get(letter, 0)

    for letter in string: 
        if chars[letter] ==1:
            return letter    
    return None

# print( first_non_repeating_char('leetcode') )

# print( first_non_repeating_char('hello') )

# print( first_non_repeating_char('aabbcc') )


def two_sum(nums, target):
    differenceMap = {}
    for i in range(len(nums)): 
        difference = target - nums[i]
     
        if difference in differenceMap:
            return [differenceMap[difference], i]
        else: 
            differenceMap[nums[i]] = i
    return None
     
        
        
    
    
    
    
print(two_sum([5, 1, 7, 2, 9, 3], 10))  
print(two_sum([4, 2, 11, 7, 6, 3], 9)) 