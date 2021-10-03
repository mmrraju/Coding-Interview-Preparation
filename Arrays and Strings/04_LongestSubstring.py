'''
Given a string s, find the length of the longest substring without repeating characters
'''

class Solution:
    def lengthOfLongestSubString(self, s):
        lst = []
        tmp = ''
        for x in s:
            if x not in tmp:
                tmp +=x 
            else:
                lst.append(len(tmp))
                tmp = tmp[tmp.index(x)+1:] + x 
        lst.append(len(tmp))
        
        return max(lst)
        
input_string = input()

obj = Solution()

print(obj.lengthOfLongestSubString(input_string))



``` Using hash table  ```
class Solution:
    def lengthOfLongestSubString(self, s):
        start = 0
        dic = {}
        max_len = 0
        for i in range(0, len(s)):
            if s[i] in dic.keys():
                prev_index = dic[s[i]]+1 
                for k in range(start, prev_index):
                    del dic[s[k]]
                dic[s[i]] = i
                start = prev_index
            else:
                dic[s[i]] = i 
            max_len = max((i-start)+1, max_len)
            
        return max_len
        
input_string = input()

obj = Solution()

print(obj.lengthOfLongestSubString(input_string))

