#Time Complexity:: Average: O(n)-Traversing set with a loop
#Space Complexity:: Almost O(1) -count of unique characters
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashset = set()
        count=0
        
        for ch in s:
            if ch not in hashset:
                hashset.add(ch)
            else:
                hashset.remove(ch)
                count+=2
        if len(hashset)!=0:
            count+=1
        
        return count
