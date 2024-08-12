# Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

# Please implement encode and decode

def encode(strs):
    #iterate through each str in strings then join by comma
    result = ""
    for s in strs: 
        result += str(len(s)) +"*"+ s
    return result

def decode(s):
    result = []
    i = 0 
    while i < len(s):
        j = i 
        while s[j] != "*":
                j+=1
        length = int(s[i:j])
        i = j+1
        j = i + length
        result.append(s[i:j])
        i = j
    return result   


print(encode(["I", "Love", "You"]))

