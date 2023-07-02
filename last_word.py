'''58. Length of Last Word

Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal 
substring
 consisting of non-space characters only.'''


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word=s.split()
        return (len(word[-1]))
        # a=0
        # for i in range(len(word)-1,-1,-1):
        #     if (len(word[i])>0):
        #         a=len(word[i])

        # return a
