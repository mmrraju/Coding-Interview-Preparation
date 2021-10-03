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
