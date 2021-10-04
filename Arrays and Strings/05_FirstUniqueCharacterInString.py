""" Given a string s, find the first non-repeating character in it and return its index.  """

s = input()

for x in s:
    if x not in s[s.index(x)+1: ]: # s.index(x) return the positions.
        print(s.index(x))
        break
        
