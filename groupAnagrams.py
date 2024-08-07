# Input: strs = ["act","pots","tops","cat","stop","hat"]

# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
from collections import defaultdict

def groupAnagrams(strs):
    #set default list to hold grouped anagrams  
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