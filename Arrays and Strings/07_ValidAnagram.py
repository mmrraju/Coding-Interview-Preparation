""" Given two strings s and t, return true if t is an anagram of s, and false otherwise. """
s = input()
t = input()

def IsValidAnagram(s, t):
        if len(s) != len(t):
            return False
        d = {}
        for ch in s:  # Making d for value count
            if ch not in d:
                d[ch] = 1
            else:
                d[ch] += 1
                
        for ch in t:  
            if ch not in d:    # if char not in d 
                return False
            else:                 #if char present chech the count and reduce it
                if d[ch] > 1:
                    d[ch] -= 1
                else:              # if char less then 1 and again appear delete it
                    del d[ch]
        return True
        
print(isMagazineInRansomNote(s, t))
