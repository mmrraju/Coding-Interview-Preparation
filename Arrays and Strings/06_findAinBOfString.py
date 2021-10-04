""" Given two stings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote """

magazine = input()
ransomNote = input()

def isMagazineInRansomNote(magazine, ransomNote):
        d = {}
        for ch in magazine:
            if ch not in d:
                d[ch] = 1
            else:
                d[ch] += 1
                
        for ch in ransomNote:  
            if ch not in d:
                return False
            else:        #if char present chech the count and reduce it
                if d[ch] > 1:
                    d[ch] -= 1
                else:   # if char less then 1 and again appear delete it
                    del d[ch]
        return True
            
print(isMagazineInRansomNote(magazine, ransomNote))
