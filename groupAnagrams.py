#Our task is to find all the words that are anagrams of each other and group them together.
# Input: strs = ["act","pots","tops","cat","stop","hat"]

# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
from collections import defaultdict

def groupAnagrams(strs):
    #default provides a default value for missing keys.
    ans = defaultdict(list)

    #For each each str in strs, set count array to have key for each letter a -z 
    for str in strs: 
        count = [0] * 26

        #for each letter in the string, update the count to represent each letter 
        for letter in str:
            count[ord(letter) - ord("a")] +=1
        #print(count)

        #convert count to tuple to use as dictionary key 
        ans[tuple(count)].append(str)

    #return values 
    return ans.values()

print(groupAnagrams(["rat", "tar"]))
print(groupAnagrams(["act","pots","tops","cat","stop","hat"]))