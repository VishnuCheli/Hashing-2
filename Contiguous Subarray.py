#Time Complexity:: Average: O(n)-Traversing hashmap with a loop
#Space Complexity:: Almost O(1) -count only changes
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No

class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #start with 0 in -1 to calculate a subarray at the start of the array
        hashmap = {0:-1} #Hashmap to store current rSum occured number and corrosponding index
        rSum=0 #running Sum
        ML=0 #Max length
        #result=[0,0]
        for i in range(len(nums)):
            if nums[i]==0:
                rSum -= 1
            else:
                rSum += 1
                
            if rSum not in hashmap:
                hashmap[rSum] = i #add the occured rSum and it's first occuring index
            else:
                if ML<(i-hashmap[rSum]):
                    ML = i-hashmap[rSum]
                    #result[1] = i+1 #setting upper bound for longest subarray
                    #result[0] = (i+1) - ML #setting lower bound for longest subarray
        #print(nums[result[0],result[1]])
        return ML
                   